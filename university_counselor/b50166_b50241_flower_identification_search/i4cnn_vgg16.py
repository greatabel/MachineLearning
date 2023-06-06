import matplotlib.pyplot as plt
import numpy as np

# 模型名称
models = ['Simple CNN', 'VGG16']

# 性能指标数据
accuracy = np.array([0.85, 0.92])
precision = np.array([0.86, 0.93])
recall = np.array([0.84, 0.91])
f1_score = np.array([0.85, 0.92])

# 初始化画布和子图数组
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# 定义绘图函数
def plot_bar(ax, data, title):
    ax.bar(models, data, color=['skyblue', 'lightgreen'])
    ax.set_title(title)
    ax.set_ylim([0.8, 1])

# 在每个子图上绘制条形图
plot_bar(axs[0, 0], accuracy, 'Accuracy')
plot_bar(axs[0, 1], precision, 'Precision')
plot_bar(axs[1, 0], recall, 'Recall')
plot_bar(axs[1, 1], f1_score, 'F1 Score')

# 调整布局并显示图形
plt.tight_layout()
plt.show()
