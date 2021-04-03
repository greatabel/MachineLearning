from flask import Flask, request
from flask import render_template
from flask import make_response

import csv
from termcolor import colored

def load(filepath):
    rows = []
    with open(filepath,'rt')as f:
      data = csv.reader(f)
      for row in data:
            # print(row, len(row))
            rows.append(row)
    return rows


app = Flask(__name__)
app.debug = True

# 目标id， 目标name相似度， 目标bio相似度，目标头像相似度
mydict = {
    1: [3, 1.0, 0.391, 0.685],
    2: [2, 0.0, 0.257, 0.604],
    3: [2, 0.0, 0.257, 0.604]
}

@app.route('/find_connect/')
@app.route('/find_connect/<index_id>')
def scp2(index_id=""):

    d_rows = load('../data/douban.csv')
    print(colored('数据集分割线'+'-'*30, 'red'))
    w_rows = load('../data/weibo.csv')
    index = ''
    target = ''
    scores = ''

    query_value = request.args.get('query')
    print('query_value=', query_value)
    if query_value != None:
        s_row = None
        for row in d_rows:
            if row[1] == query_value:
                # print(row[1], ' here', row)
                s_row = row

        index = str(s_row)
        s_values = mydict[int(s_row[0])]
        print(s_values, '#'*20) 
        t_row = None
        for row in w_rows:
            # print(row[1],s_values[0], type(s_values[0]))
            if int(row[0]) == s_values[0]:
                # print(row[0], ' here', row)
                t_row = row
        target = str(t_row)
        scores = str(s_values[1:])
        # print('scores=', scores)
        print(colored('scores'+'-'*30, 'red'),scores)
    r = make_response(
        render_template('scp2.html', query_value=query_value,index=index, 
            target=target,scores=scores)
        )

    return r


@app.route('/find_5connect/')
@app.route('/find_5connect/<index_id>')
def scp5(index_id=""):

    d_rows = load('../data/douban.csv')
    print(colored('数据集分割线'+'-'*30, 'red'))
    w_rows = load('../data/weibo.csv')
    index = ''
    target = ''
    scores = ''

    query_value = request.args.get('query')
    print('query_value=', query_value)
    if query_value != None:
        s_row = None
        for row in d_rows:
            if row[1] == query_value:
                # print(row[1], ' here', row)
                s_row = row

        index = str(s_row)
        s_values = mydict[int(s_row[0])]
        print(s_values, '#'*20) 

        # hardcode 
        matched_ids = [2, 1, 3, 4, 5]
        scores = [0.89, 0.72, 0.71, 0.51, 0.59, 0.41]
        t_rows = []
        j = 0
        for i in matched_ids:

            x = w_rows[i-1]
            print(x)
            x.append(scores[j])
            t_rows.append(x)
            j += 1
        

        # print('scores=', scores)
        print(colored('scores'+'-'*30, 'red'),scores)
        print(t_rows)
    r = make_response(
        render_template('scp5.html', query_value=query_value,index=index, 
            t_rows=t_rows)
        )
    # http://127.0.0.1:5000/find_5connect/?query=krugman
    return r



if __name__ == '__main__':
    app.run()