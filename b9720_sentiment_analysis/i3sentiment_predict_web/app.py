from flask import Flask, request
from flask import render_template
from flask import make_response


from predict_realdata import flow_predict

app = Flask(__name__)
app.debug = True


@app.route('/predict/')
@app.route('/predict/<index_id>')
def scp2(index_id=""):

    index = ''

    query_value = request.args.get('comment')
    print('comment=', query_value)
    if query_value != None:

	    result = flow_predict(query_value)
	    index = str(result) + " !!!"
    r = make_response(
        render_template('scp2.html', query_value=query_value,index=index)
        )

    return r




if __name__ == '__main__':
    app.run()