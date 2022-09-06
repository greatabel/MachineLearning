import pydoop.hdfs as hdfs


b = hdfs.path.isdir("/data")

# 例子
want_file = 'test_format2.csv'

if b == True:
    print("---get test ---")
    lines = []
    with hdfs.open("hdfs://127.0.0.1:9000/data/"+want_file) as f:
        for line in f:
            # print(line, type(line))
            l = line.decode("utf-8")
            if l is not None and l != "":
                lines.append(l)
    print(lines)
    print("---end get----")

    with open("i8predict_flow/"+want_file, "wb") as myfile:
        myfile.write(str(lines))
