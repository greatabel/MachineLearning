import re

print('Better understand ./data/ap/ap.dat and ap.txt')
with open("./data/ap/ap.txt") as f:
    contents = f.read()
    count = sum(1 for x in re.finditer(r"<DOC>", contents))
    print(count)

with open("./data/ap/ap.dat") as f:
    contents = f.read()
    countB = sum(1 for x in re.finditer(r"\n", contents))
    print(countB)

ap_txt_9 = "Here is a summary of developments in forest and brush fires in Western states:"
ap_dat_9 = "7 5829:1 4040:1 2891:1 14:1 1783:1 381:1 2693:1"
print("ap.txt 第9项是:\n" + 
        ap_txt_9)
print("ap.dat 第9项是:\n" +
        ap_dat_9)
