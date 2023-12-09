#第4章/列出可用的评价指标
from datasets import list_metrics

metrics_list = list_metrics()

print(	len(metrics_list), metrics_list[:5] )
print('-'*20)

from datasets import load_metric

metric = load_metric(path='glue', config_name='mrpc')

print(metric.inputs_description)

#第4章/计算一个评价指标
predictions = [0, 1, 0]
references = [0, 1, 1]

m = metric.compute(predictions=predictions, references=references)

print('-'*20)
print(m)