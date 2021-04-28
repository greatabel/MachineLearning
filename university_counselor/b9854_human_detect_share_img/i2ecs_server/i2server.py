import os
from flask import Flask, request, Response
from flask import render_template
import jsonpickle
import numpy as np
import cv2


from MyQR import myqr

addr = 'http://localhost:5000'
test_url = addr + '/api/test'

# Initialize the Flask application
app = Flask(__name__)
app.debug = True


PEOPLE_FOLDER = os.path.join('static', 'received')

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

print('instance_path=', app.root_path)
index = 0

# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():

    global index
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    saved_dir = app.root_path + '/static/received'
    print(saved_dir, '#'*20)
    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    if len(img) > 10:
        cv2.imwrite("static/received/"+str(index) + ".png", img)
        myqr.run(
            words=addr +'/image?index='+str(index),
            # 扫描二维码后，显示的内容，或是跳转的链接
            version=5,  # 设置容错率
            level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
            picture= app.root_path + '/bg.png',  # 图片所在目录，可以是动图
            colorized=True,  # 黑白(False)还是彩色(True)
            contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
            brightness=1.0,  # 用来调节图片的亮度，用法同上。
            save_name=str(index)+'_qr.png',  # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
            save_dir= saved_dir
        )

        index += 1
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


@app.route('/')
@app.route('/image')
def show_image():
    args = request.args
    index = '0'
    if 'index' in args and args['index'] != None:
        index = args['index']

    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], index + '.png')
    print(full_filename)
    return render_template("image.html", user_image = full_filename)

# start flask app
app.run(host="0.0.0.0", port=5000)