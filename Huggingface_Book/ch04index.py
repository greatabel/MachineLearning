#第4章/列出可用的评价指标
from datasets import list_metrics

metrics_list = list_metrics()

print(	len(metrics_list), metrics_list[:5] )