import re

with open("./data/ap/ap.txt") as f:
    contents = f.read()
    count = sum(1 for x in re.finditer(r"<DOC>", contents))
    print(count)

with open("./data/ap/ap.dat") as f:
    contents = f.read()
    countB = sum(1 for x in re.finditer(r"\n", contents))
    print(countB)