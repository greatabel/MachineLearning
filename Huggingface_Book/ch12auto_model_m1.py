#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========================================
# 🔧 配置区域 - 在这里修改参数
# ========================================
DATA_PERCENT = 0.1  # ← 修改这里！ 0.1 = 10%, 0.5 = 50%, 1.0 = 100%
BATCH_SIZE = 16
NUM_EPOCHS = 1
LEARNING_RATE = 5e-4
# ========================================

# ====== 抑制所有警告（必须放在最前面） ======
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'

import warnings
warnings.filterwarnings('ignore')
import logging
logging.disable(logging.CRITICAL)

# ====== 加载编码工具 ======
from transformers import BertTokenizer
token = BertTokenizer.from_pretrained('bert-base-chinese')
print("✅ 已加载 BertTokenizer")

# ====== 加载数据集 ======
from datasets import load_from_disk
dataset = load_from_disk('./data/ChnSentiCorp')
print("✅ 已加载数据集")

# ====== M1 Mac GPU 加速配置 ======
import torch
device = 'cpu'

if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
    device = 'mps'
    print("✅ 使用 M1 GPU 加速 (MPS)")
else:
    print("⚠️  MPS 不可用，使用 CPU")

print(f"计算设备: {device}")

# ====== 按百分比加载数据 ======
train_size = int(len(dataset['train']) * DATA_PERCENT)
val_size = int(len(dataset['validation']) * DATA_PERCENT)
test_size = int(len(dataset['test']) * DATA_PERCENT)

train_dataset = dataset['train'].select(range(train_size))
val_dataset = dataset['validation'].select(range(val_size))
test_dataset = dataset['test'].select(range(test_size))

print(f"\n📊 数据量配置（{DATA_PERCENT*100:.0f}%）：")
print(f"  训练集: {len(train_dataset):,} / {len(dataset['train']):,} 样本")
print(f"  验证集: {len(val_dataset):,} / {len(dataset['validation']):,} 样本")
print(f"  测试集: {len(test_dataset):,} / {len(dataset['test']):,} 样本")

# ====== 数据整理函数 ======
def collate_fn(data):
    sents = [i['text'] for i in data]
    labels = [int(i['label']) for i in data]
    data = token.batch_encode_plus(batch_text_or_text_pairs=sents,
                                   truncation=True,
                                   padding=True,
                                   max_length=512,
                                   return_tensors='pt')
    for k, v in data.items():
        data[k] = v.to(device)
    data['labels'] = torch.LongTensor(labels).to(device)
    return data

# ====== 数据加载器 ======
loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                     batch_size=BATCH_SIZE,
                                     collate_fn=collate_fn,
                                     shuffle=True,
                                     drop_last=True)
print(f"\n✅ 数据加载器已创建，共 {len(loader)} 个 batch")

# ====== 查看数据样例 ======
print("\n查看第一个 batch 的数据：")
for i, data in enumerate(loader):
    break
for k, v in data.items():
    print(f"  {k}: {v.shape}")

# ====== 加载预训练模型 ======
print("\n加载预训练模型...")
from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained('bert-base-chinese',
                                                           num_labels=2)
model.to(device)

# ====== 模型参数量显示（B 单位） ======
param_count = sum(i.numel() for i in model.parameters())

if param_count >= 1e9:
    param_str = f"{param_count / 1e9:.2f}B"
elif param_count >= 1e6:
    param_str = f"{param_count / 1e6:.2f}M"
else:
    param_str = f"{param_count / 1e3:.2f}K"

print(f"✅ 模型参数量: {param_str}")

# ====== 模型试算 ======
print("\n模型试算:")
out = model(**data)
print(f"  loss: {out['loss']:.4f}")
print(f"  logits shape: {out['logits'].shape}")

# ====== 训练函数 ======
from transformers import AdamW
from transformers.optimization import get_scheduler

def train(num_epochs=NUM_EPOCHS):
    optimizer = AdamW(model.parameters(), lr=LEARNING_RATE)
    scheduler = get_scheduler(name='linear',
                              num_warmup_steps=0,
                              num_training_steps=len(loader) * num_epochs,
                              optimizer=optimizer)
    
    model.train()
    
    for epoch in range(num_epochs):
        print(f"\n{'='*60}")
        print(f"Epoch {epoch + 1}/{num_epochs}")
        print(f"{'='*60}")
        total_loss = 0
        
        for i, batch_data in enumerate(loader):
            out = model(**batch_data)
            loss = out['loss']
            total_loss += loss.item()
            
            loss.backward()
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad()
            
            if i % 5 == 0:  # 每 5 个 batch 输出
                pred = out['logits'].argmax(dim=1)
                labels = batch_data['labels']
                accuracy = (pred == labels).sum().item() / len(labels)
                lr = optimizer.state_dict()['param_groups'][0]['lr']
                print(f"  Batch {i:3d}/{len(loader):3d}: loss={loss.item():.4f}, acc={accuracy:.4f}")
        
        avg_loss = total_loss / len(loader)
        print(f"✓ Epoch {epoch + 1} 平均 loss: {avg_loss:.4f}")

print("\n🚀 开始训练...")
import time
start_time = time.time()
train(num_epochs=NUM_EPOCHS)
elapsed = time.time() - start_time
print(f"⏱️  训练耗时: {elapsed:.1f} 秒")

# ====== 测试函数 ======
def test():
    loader_test = torch.utils.data.DataLoader(dataset=test_dataset,
                                              batch_size=BATCH_SIZE,
                                              collate_fn=collate_fn,
                                              shuffle=False,
                                              drop_last=False)
    model.eval()
    correct = 0
    total = 0
    
    print(f"\n{'='*60}")
    print("开始测试...")
    print(f"{'='*60}")
    
    for i, batch_data in enumerate(loader_test):
        with torch.no_grad():
            out = model(**batch_data)
        
        pred = out['logits'].argmax(dim=1)
        labels = batch_data['labels']
        correct += (pred == labels).sum().item()
        total += len(labels)
    
    accuracy = correct / total
    print(f"\n✅ 测试准确率: {accuracy:.4f} ({correct}/{total})")
    return accuracy

test_acc = test()

print("\n" + "="*60)
print("✅ 所有步骤完成！")
