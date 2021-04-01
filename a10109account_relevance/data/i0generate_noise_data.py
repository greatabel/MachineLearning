import random,string

first_name = ["王", "猫", "独立", "刘", "赵", "蒋", "孟", "陈", "徐", 
	"杨", "沈", "马", "高", "殷", "上官", "钟", "常"]
second_name = ["伟墙头", "华头", "建国", "洋头", "刚", "万里", "爱民", 
	"牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷", "文","明浩", "光", "超", "军", "达"]
name = random.choice(first_name) + random.choice(second_name)

#生成大小字母和数字一起的大字符串
all_str = string.ascii_letters+string.digits

res_lit = []
#生成100个
for i in range(24):
    #从大字符串中随机生成8位数的字符，换行并转换成字符串
	res0  =  ''.join(random.sample(all_str,4))
	res  =  ''.join(random.sample(all_str,8))
	bio  = 'noise data '+ ''.join(random.sample(all_str,30))
	if res not in res_lit:
		if i > 3:
			print(str(i)+","+ res0+","+res+",'上海','"+bio+"'")
		res_lit.append((i,res))


print('-'*30)

for i in range(24):
    #从大字符串中随机生成8位数的字符，换行并转换成字符串
	res0  =  ''.join(random.sample(all_str,5))
	name = random.choice(first_name) + random.choice(second_name)
	res  =  ''.join(random.choice("0123456789") for i in range(16))
	bio  = 'noise data '+ ''.join(random.sample(all_str,30)) + \
	 random.choice(second_name) + ' ' + random.choice(second_name)
	if res not in res_lit:
		if i > 3:
			print(str(i)+","+res+","+name+",'上海','"+bio+"'")
		res_lit.append((i,res))
