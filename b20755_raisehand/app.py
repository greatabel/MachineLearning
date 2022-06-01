import base64
import os
import uuid

from PIL import Image
from flask import Flask, render_template, request
from flask import url_for
from flask import redirect

from flask import Response, session
from flask import Blueprint, jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import flask_login
from sqlitedict import SqliteDict


from flask_script import Manager
import train
import face_recognition
from model import User


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meeting.db'
db = SQLAlchemy(app)

# manager = Manager(app)
app.config["secret_key"] = "abelTest"
app.secret_key = "abelTest"
train.init()
app.debug = True


signed_users = []


# -------start 课堂管理 ---------


class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    participants = db.Column(db.String(80), nullable=True)
    host = db.Column(db.String(80), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):
        return '<Meeting %r>' % self.name


@app.route('/meetinglist', methods=['GET', 'POST'])
def meeting_list():
    if request.method == 'POST':
        name = request.form['name']
        participants = request.form['participants']
        host = request.form['host']
        new_stuff = Meeting(name=name, participants=participants, host=host)

        try:
            db.session.add(new_stuff)
            db.session.commit()
            return redirect('/meetinglist')
        except:
            return "There was a problem adding new stuff."

    else:
        groceries = Meeting.query.order_by(Meeting.created_at).all()
        return render_template('list.html', groceries=groceries)


@app.route('/meeting_delete/<int:id>')
def meeting_delete(id):
    meeting = Meeting.query.get_or_404(id)

    try:
        db.session.delete(meeting)
        db.session.commit()
        return redirect('/meetinglist')
    except:
        return "There was a problem deleting data."


@app.route('/meeting_update/<int:id>', methods=['GET', 'POST'])
def meeting_update(id):
    meeting = Meeting.query.get_or_404(id)

    if request.method == 'POST':
        meeting.name = request.form['name']
        meeting.participants = request.form['participants']
        meeting.host = request.form['host']

        try:
            db.session.commit()
            return redirect('/meetinglist')
        except:
            return "There was a problem updating data."

    else:
        title = "Update Data"
        return render_template('update.html', title=title, meeting=meeting)

# -------end   课堂管理 ---------


# -------start 注册登录 ---------

stored_user = None
login_manager = flask_login.LoginManager(app)

# https://pypi.org/project/sqlitedict/
user_pass = SqliteDict("my_db.sqlite", autocommit=True)

"""
使用 https://flask-login.readthedocs.io/en/0.3.1/ 
库进行用户登录凭证的验证
"""
@app.route("/get_signed_users")
def get_signed_users():
    global signed_users
    print('in signed_users func', signed_users)
    return jsonify(results = signed_users)


@app.route("/save_meeting")
def save_meeting_to_db():
    global signed_users

    historys = user_pass.get('meeting_history', None)
    print('historys=', historys, '#'*10)
    from time import gmtime, strftime
    nowdt = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    record = (session['username'], signed_users, nowdt)

    if historys is None:
        historys = []
        print('historys is emppty' )        
        user_pass['meeting_history'] = [record]
    else:
        import copy
        new_historys = copy.deepcopy(historys)
        # new_historys.append(record)
        new_historys.insert(0,record)
        user_pass['meeting_history'] = new_historys
    print('save_meeting')
    return jsonify(results ='ok'), 200




@login_manager.user_loader
def load_user(email):
    return user_pass.get(email, None)


"""
登录相关后端接口，验证凭证，根据是否通过进行跳转和提示
"""


@app.route("/login", methods=["POST", "GET"])
def login():
    """login function

    login function

    Args:
        email, password

    Returns:
        edirect "home_bp.home"
    """
    global stored_user
    email = request.form.get("email")
    password = request.form.get("password")
    stored_user = user_pass.get(email, None)
    if stored_user and password == stored_user.password:

        flask_login.login_user(stored_user)
        session["username"] = stored_user.user_name
        print(stored_user.is_active, "login")
        return redirect(url_for("index"))
    else:
        print("login fail")
    return redirect(url_for("home", pagenum=1))


"""
登录相关后端接口，验证凭证，根据是否通过进行跳转和提示
"""


@app.route("/register", methods=["POST"])
def register():
    """register function

    @@@
    #### args

    | args | nullable | type | remark |
    |--------|--------|--------|--------|
    |    email    |    password    |    password2

    #### return
    - ##### json
    > redirect(url_for("home_bp.home", pagenum=1))
    @@@
    """
    email = request.form.get("email")
    pw1 = request.form.get("password")
    pw2 = request.form.get("password2")
    if not pw1 == pw2:
        session["username"] = email
        return redirect(url_for("home", pagenum=1))
    # if DB.get_user(email):
    if email in user_pass:
        print("already existed user")
        return redirect(url_for("home", pagenum=1))
    # salt = PH.get_salt()
    # hashed = PH.get_hash(pw1 + salt)
    print("register", email, pw1)
    user = User(email, pw1)
    user_pass[email] = user
    # print("register", user_pass, "#" * 5)
    return redirect(url_for("home", pagenum=1))


"""
登出网站相关后端接口，根据是否通过进行跳转和提示
"""


@app.route("/logout")
def logout():
    """logout function

    @@@
    #### args



    #### return
    - ##### json
    > redirect(url_for("home_bp.home", pagenum=1))
    @@@
    """
    flask_login.logout_user()
    return redirect(url_for("home", pagenum=1))


@app.route("/home")
def home():
    historys = user_pass.get('meeting_history', None)
    return render_template("home.html", historys=historys)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# android端调用api
@app.route("/uploadhc/<name>", methods=['POST'])
def uploadhc(name):
    print('in uploadhc', '>'*10, name)
    target = os.path.join(APP_ROOT, "trained_images/"+name)


    if not os.path.isdir(target):
        os.mkdir(target)
    print('#'*20, ' in uploadhc ', target, '#'*5,request.files)
    # if 'file' not in request.files:
    #     error = "Missing data source!"
    #     return jsonify({'error': error})


    file = request.files['uploadImg1']
    fileName = "testha.jpg"
    destination = '/'.join([target, fileName])
    file.save(destination)


    success = "Success!"
    return jsonify({'file': success})


# -------end   注册登录 ---------


@app.route("/index")
def index():
    global signed_users
    # print(signed_users, '#'*10, 'index')
    return render_template("index.html")


@app.route("/pichandler", methods=["post", "get"])
def pichandler():
    name = ""
    locations = ""

    pic_data_url = request.form.get("picdata")
    # print(">>>>>>>",request.form.get('picdata'))
    imgdata = base64.b64decode(pic_data_url.split(",")[1])
    with open("temp3.jpg", "wb") as f:  # 把上传图片保存为文件，！！！有待优化
        f.write(imgdata)

    # pic = request.files.get("myPic")  # 上传图片
    # print("pic:",pic)

    reconize_result = train.recognize_from_upload("temp3.jpg")  # 识别结果
    print("Recognize_result:", reconize_result)
    print(type(reconize_result))
    for i in reconize_result[0]:
        if name == "":
            name = i
        else:
            name = name + "," + i
    for i in reconize_result[1]:
        if locations == "":
            locations = i
        else:
            locations = str(locations) + ";" + str(i)

    return str(name) + "-" + str(locations)


@app.route("/update", methods=["post", "get"])
def update():
    pic_data_url = request.form.get("picdata")
    imgdata = base64.b64decode(pic_data_url.split(",")[1])

    with open("temp.jpg", "wb") as f:  # 把上传图片保存为文件，！！！有待优化
        f.write(imgdata)
    known_image = face_recognition.load_image_file("temp.jpg")
    name_list = request.form.get("name").split(",")  # 上传名字
    print("need_to_update:", name_list)
    for name in name_list:  # * 为内容未改变
        if name != "*":
            #  known_encoding = face_recognition.face_encodings(known_image)[name_list.index(name)]
            # 对改变名字的脸部信息编码
            face_location = face_recognition.face_locations(known_image)[
                name_list.index(name)
            ]
            top, right, bottom, left = face_location
            face_image = known_image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            if not os.path.exists("trained_images/" + name):
                os.mkdir("trained_images/" + name)
            uuid_str = uuid.uuid4().hex
            pil_image.save("trained_images/" + name + "/" + uuid_str + ".jpg")  # 保存图片
            train.add_data(name, "trained_images/" + name + "/" + uuid_str + ".jpg")

    # print(known_encoding)
    return "success"


@app.route("/vidohandler", methods=["get", "post"])
def vido_handler():
    global signed_users
    name = ""
    locations = ""
    pic_data_url = request.form.get("picdata")
    imgdata = base64.b64decode(pic_data_url.split(",")[1])

    with open("temp2.jpg", "wb") as f:  # 把上传图片保存为文件，！！！有待优化
        f.write(imgdata)
    reconize_result = train.recognize_from_upload("temp2.jpg")  # 识别结果
    print("reconize_result:", reconize_result)
    if reconize_result == "noface":
        return reconize_result
    for i in reconize_result[0]:
        if name == "":
            name = i
        else:
            name = name + "," + i
    for i in reconize_result[1]:
        if locations == "":
            locations = i
        else:
            locations = str(locations) + ";" + str(i)

    print("#" * 30, str(name) + "-" + str(locations))
    # 代表多人的情况
    if ',' in name:
        names = name.split(',')
        for n in names:
            if n != "somebody" and n not in signed_users:
                signed_users.append(n)
    else:
    # 单人情况
        if name != "somebody" and name not in signed_users:
            signed_users.append(name)

    return str(name) + "-" + str(locations)


@app.route("/testjpg", methods=["post", "get"])
def testjpg():
    pic_data_url = request.form.get("picdata")

    imgdata = base64.b64decode(pic_data_url.split(",")[1])

    with open("temp3.jpg", "wb") as f:
        f.write(imgdata)
    return "success"


if __name__ == "__main__":
    # app.run(host="127.0.0.1", port="5000", ssl_context="adhoc")
    app.run(host="127.0.0.1", port=5000)