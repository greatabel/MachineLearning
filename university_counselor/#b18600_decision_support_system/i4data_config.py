'''

"London Central Hostel"
"Coca-Cola London Eye"
此处我们假设分析的是2个地方，我们有了先验的游客地域偏好，景点质量的偏好
然后做推断
'''
header = [('location', 'cost'),
          ('quality', 'cost'),
          ('cost', 'no_of_people'),
          ('location', 'no_of_people')]
location_distribute = [[0.6], [0.4]]
quality_distribute = [[0.3], [0.5], [0.2]]

