import re
from termcolor import colored


#  https://github.com/blei-lab/lda-c/blob/master/readme.txt

print('Better understand ./data/ap/ap.dat and ap.txt')
with open("./data/ap/ap.txt") as f:
    contents = f.read()
    countA = sum(1 for x in re.finditer(r"<DOC>", contents))
    print(countA)

with open("./data/ap/ap.dat") as f:
    contents = f.read()
    countB = sum(1 for x in re.finditer(r"\n", contents))
    print(countB)

print(colored('*'*25, 'red'))
if countA == countB:
    print("1. 至少暗示了ap.txt和ap.dat的1 <---> 1 对应关系！")



ap_txt_9 = "Here is a summary of developments in forest and brush fires in Western states:"
ap_dat_9 = "7 5829:1 4040:1 2891:1 14:1 1783:1 381:1 2693:1"
print("ap.txt 第9项是:\n" + 
        ap_txt_9)
print("ap.dat 第9项是:\n" +
        ap_dat_9)

vocab = None
with open("./data/ap/vocab.txt") as f:
    vocab = f.readlines()
vocab = [x.strip() for x in vocab] 
print("len(vocab)=", len(vocab))

ap_dic = {}
for i in ap_dat_9.split()[1:]:
    i_split = i.split(':')
    ap_dic[int(i_split[0])] = int(i_split[1])
for k,v in ap_dic.items():
    print(vocab[k], end='\t')
    ap_txt_9 = ap_txt_9.lower().replace(vocab[k], "")
print("\nremain=", ap_txt_9)

print(colored('*'*25, 'red'))
print("2. 这说明了ap.dat里面只是vocab.txt词汇在ap.txt每一项中出现的总数和单个次数。")