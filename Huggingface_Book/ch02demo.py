#!/usr/bin/env python
# coding: utf-8

# In[1]:


#字典
vocab = {
    '<SOS>': 0,
    '<EOS>': 1,
    'the': 2,
    'quick': 3,
    'brown': 4,
    'fox': 5,
    'jumps': 6,
    'over': 7,
    'a': 8,
    'lazy': 9,
    'dog': 10,
}


# In[ ]:





# In[2]:


#添加首尾符号
sent = 'the quick brown fox jumps over a lazy dog'

sent = '<SOS> ' + sent + ' <EOS>'

print(sent)


# In[3]:


#英文分词
words = sent.split()

print(words)


# In[4]:


#编码为数字
encode = [vocab[i] for i in words]

print(encode)


# In[5]:


#第2章/加载编码工具
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained(
    pretrained_model_name_or_path='bert-base-chinese',
    cache_dir=None,
    force_download=False,
)

tokenizer


# In[6]:


#第2章/准备实验数据
sents = [
    '你站在桥上看风景',
    '看风景的人在楼上看你',
    '明月装饰了你的窗子',
    '你装饰了别人的梦',
]


# In[7]:


#第2章/基本的编码函数
out = tokenizer.encode(
    text=sents[0],
    text_pair=sents[1],

    #当句子长度大于max_length时截断
    truncation=True,

    #一律补pad到max_length长度
    padding='max_length',
    add_special_tokens=True,
    max_length=25,
    return_tensors=None,
)

print(out)
print(tokenizer.decode(out))


# In[8]:


#第2章/进阶的编码函数
out = tokenizer.encode_plus(
    text=sents[0],
    text_pair=sents[1],

    #当句子长度大于max_length时截断
    truncation=True,

    #一律补零到max_length长度
    padding='max_length',
    max_length=25,
    add_special_tokens=True,

    #可取值tf,pt,np,默认为返回list
    return_tensors=None,

    #返回token_type_ids
    return_token_type_ids=True,

    #返回attention_mask
    return_attention_mask=True,

    #返回special_tokens_mask 特殊符号标识
    return_special_tokens_mask=True,

    #返回length 标识长度
    return_length=True,
)

#input_ids 编码后的词
#token_type_ids 第一个句子和特殊符号的位置是0,第二个句子的位置是1
#special_tokens_mask 特殊符号的位置是1,其他位置是0
#attention_mask pad的位置是0,其他位置是1
#length 返回句子长度
for k, v in out.items():
    print(k, ':', v)

tokenizer.decode(out['input_ids'])


# In[9]:


#第2章/批量编码成对的句子
out = tokenizer.batch_encode_plus(
    #编码成对的句子
    batch_text_or_text_pairs=[(sents[0], sents[1]), (sents[2], sents[3])],
    
    add_special_tokens=True,

    #当句子长度大于max_length时截断
    truncation=True,

    #一律补零到max_length长度
    padding='max_length',
    max_length=25,

    #可取值tf,pt,np,默认为返回list
    return_tensors=None,

    #返回token_type_ids
    return_token_type_ids=True,

    #返回attention_mask
    return_attention_mask=True,

    #返回special_tokens_mask 特殊符号标识
    return_special_tokens_mask=True,

    #返回offset_mapping 标识每个词的起止位置,这个参数只能BertTokenizerFast使用
    #return_offsets_mapping=True,

    #返回length 标识长度
    return_length=True,
)

#input_ids 编码后的词
#token_type_ids 第一个句子和特殊符号的位置是0,第二个句子的位置是1
#special_tokens_mask 特殊符号的位置是1,其他位置是0
#attention_mask pad的位置是0,其他位置是1
#length 返回句子长度
for k, v in out.items():
    print(k, ':', v)

tokenizer.decode(out['input_ids'][0])


# In[10]:


#编码单个的句子
#batch_text_or_text_pairs=[sents[0], sents[1]]


# In[11]:


#第2章/获取字典
vocab = tokenizer.get_vocab()

type(vocab), len(vocab), '明月' in vocab


# In[12]:


#第2章/添加新词
tokenizer.add_tokens(new_tokens=['明月', '装饰', '窗子'])

tokenizer.add_special_tokens({'eos_token': '[EOS]'})

vocab = tokenizer.get_vocab()

type(vocab), len(vocab), vocab['明月'], vocab['[EOS]']


# In[13]:


#第2章/编码新添加的词
out = tokenizer.encode(
    text='明月装饰了你的窗子[EOS]',
    text_pair=None,

    #当句子长度大于max_length时,截断
    truncation=True,

    #一律补pad到max_length长度
    padding='max_length',
    add_special_tokens=True,
    max_length=10,
    return_tensors=None,
)

print(out)

tokenizer.decode(out)


# In[ ]:




