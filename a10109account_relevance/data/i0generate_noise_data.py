import random,string

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
	res  =  ''.join(random.choice("0123456789") for i in range(16))
	bio  = 'noise data '+ ''.join(random.sample(all_str,30))
	if res not in res_lit:
		if i > 3:
			print(str(i)+","+res0+","+res+",'上海','"+bio+"'")
		res_lit.append((i,res))
