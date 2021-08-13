import csv
from datetime import datetime, timedelta

'''
根据csv原始数据中： 窑味料量、头煤的变化 去掉一定前后区间的间跃值

 10秒
 10分
 1小时

 https://stackoverflow.com/questions/16286991/converting-yyyy-mm-dd-hhmmss-date-time

'''
targe_filename = "/GlobalSickinfo_20210412.csv"

path = "data/" + targe_filename

#实际处理 注释掉这行
# path = "HXDataSample/" + targe_filename

newpath = "processed_data/" + targe_filename

bufsize = 65536*6*3
#实际处理 注释掉这行
# bufsize = 5000

#窑味料量
Feeding_index = 28
HeadCoal_index = 29

def process(lines):
    time_need_removed = []
    rows = []
    for i in range(0, len(lines)):
        items = lines[i].split(',')
        # filter out 8900 行后有问题的部分
        if len(items) > 71:
            if items[0] is not None and '-' in items[0] and \
                items[51] is not None and items[51] != '' and items[71] !='':
                print(items[0], 'DiseName=', items[51], 'PrescrptInfo=',  items[71])
                rows.append(lines[i])
    return rows




def main():
    # header = get_header(path)
    # print('header=', header)
    # write_count = 0
    with open(path, encoding="UTF-8") as infile:
        while True:
            lines = infile.readlines(bufsize)
            print('len(lines)=', len(lines))
            if not lines:
                break

            rows = process(lines)
            # print('process len(rows)=', len(rows), rows, '-'*10, '\n')
            # for r in rows:
            #     print(r, '#'*10, '\n')
            with open(newpath, "a", newline="") as csvfile:                            
                writer = csv.writer(csvfile) 

                # if write_count == 0:
                #     writer.writerow(header)
                # write_count += 1
                for row in rows:
                    writer.writerow(row.split(','))

if __name__ == "__main__":
    main()
