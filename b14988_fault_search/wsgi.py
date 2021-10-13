"""App entry point."""
import os
import sys
import json

import flask_login
from flask_cors import CORS

from flask import send_from_directory
from flask import request
from flask import url_for
from flask import redirect, session
from flask import Blueprint, render_template as rt
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, Response
from flask import jsonify
from flask_cors import CORS
from movie import create_app
from csv_operation import csv_reader, write_to_csv

import jellyfish
# from movie.domain.model import Director, Review, Movie

# from html_similarity import style_similarity, structural_similarity, similarity
# from common import set_js_file



app = create_app()
app.secret_key = "ABCabc123"
app.debug = True
CORS(app)
# --- total requirement ----
# 1. 提供一个后台案例库系统，根据买家整理的带有解决措施和故障等级的案例库csv的中案例和部件描述，我们做好索引检索各种功能
# 2.  用户新的需要匹配的csv上传功能
# 3. 读取和分析用户上传的csv新案例库（和原来的相比，只是缺少解决措施和故障等级）内容
# 4. 检索平台在搜索结果页，根据内容相似度算法，找到最匹配的案例，然后相关解决措施和故障等级作为用户上传csv中各条故障描述的 推荐。
# 5. 一个正常的案例库系统web平台注册、登陆、登出功能


# ---start  数据库 ---

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///campus_data.db"
db = SQLAlchemy(app)

# --- end   数据库 ---
admin_list = ["admin@126.com"]



class User(db.Model):
    """Create user table"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    nickname = db.Column(db.String(80))
    school_class = db.Column(db.String(80))
    school_grade = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Blog(db.Model):
    """
    缺陷数据模型
    """

    # 主键ID
    id = db.Column(db.Integer, primary_key=True)
    # 缺陷标题
    line = db.Column(db.String(100))
    device_type = db.Column(db.String(100))
    device_part = db.Column(db.String(100))
    # 缺陷正文
    fault_content = db.Column(db.Text)

    fault_level = db.Column(db.String(100))
    response = db.Column(db.String(100))



    def __init__(self, line, device_type, device_part, fault_content, fault_level, response):
        """
        初始化方法
        """
        self.line = line
        self.device_type = device_type
        self.device_part = device_part

        self.fault_content = fault_content
        self.fault_level = fault_level
        self.response = response


# 老师当前布置缺陷的表
class TeacherWork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    detail = db.Column(db.String(500))
    answer = db.Column(db.String(5000))
    course_id = db.Column(db.Integer)

    def __init__(self, title, detail, answer, course_id):
        self.title = title
        self.detail = detail
        self.answer = answer
        self.course_id = course_id


class StudentWork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    answer = db.Column(db.String(5000))
    score = db.Column(db.DECIMAL(10, 2))
    course_id = db.Column(db.Integer)

    def __init__(self, userid, answer, score, course_id):
        self.userid = userid
        self.answer = answer
        self.score = score
        self.course_id = course_id


### -------------start of home


class PageResult:
    def __init__(self, data, page=1, number=2):
        self.__dict__ = dict(zip(["data", "page", "number"], [data, page, number]))
        self.full_listing = [
            self.data[i : i + number] for i in range(0, len(self.data), number)
        ]
        self.totalpage = len(data) // number
        print("totalpage=", self.totalpage)

    def __iter__(self):
        if self.page - 1 < len(self.full_listing):
            for i in self.full_listing[self.page - 1]:
                yield i
        else:
            return None

    def __repr__(self):  # used for page linking
        return "/home/{}".format(self.page + 1)  # view the next page


@app.route("/home/<int:pagenum>", methods=["GET"])
@app.route("/home", methods=["GET", "POST"])
def home(pagenum=1):
    print("home " * 10)
    blogs = Blog.query.all()
    user = None
    if "userid" in session:
        user = User.query.filter_by(id=session["userid"]).first()
    else:
        print("userid not in session")
    print("in home", user, "blogs=", len(blogs), "*" * 20)
    if request.method == "POST":
        search_list = []
        keyword = request.form["keyword"]
        print("keyword=", keyword, "-" * 10)
        if keyword is not None:
            for movie in notice_list:
                if movie.director.director_full_name == keyword:
                    search_list.append(movie)

                for actor in movie.actors:
                    if actor.actor_full_name == keyword:
                        search_list.append(movie)
                        break

                for gene in movie.genres:
                    if gene.genre_name == keyword:
                        search_list.append(movie)
                        break
        print("search_list=", search_list, "#" * 5)
        return rt("home.html", listing=PageResult(search_list, pagenum, 2), user=user)

    return rt("home.html", listing=PageResult(blogs, pagenum), user=user)


@app.route("/blogs/create", methods=["GET", "POST"])
def create_blog():
    """
    创建缺陷文章        
        self.line = line
        self.device_type = device_type
        self.device_part = device_part

        self.fault_content = fault_content
        self.fault_level = fault_level
        self.response = response
    """
    if request.method == "GET":
        # 如果是GET请求，则渲染创建页面
        return rt("create_blog.html")
    else:
        # 从表单请求体中获取请求数据
        line = request.form["line"]
        device_type = request.form["device_type"]
        device_part = request.form["device_part"]
        fault_content = request.form["fault_content"]
        fault_level = request.form["fault_level"]
        response = request.form["response"]

        # 创建一个缺陷对象
        blog = Blog(line=line, device_type=device_type, device_part=device_part,
                    fault_content=fault_content, fault_level=fault_level, response=response)
        db.session.add(blog)
        # 必须提交才能生效
        db.session.commit()
        # 创建完成之后重定向到缺陷列表页面
        return redirect("/blogs")


@app.route("/blogs", methods=["GET"])
def list_notes():
    """
    查询缺陷列表
    """
    blogs = Blog.query.all()
    # 渲染缺陷列表页面目标文件，传入blogs参数
    return rt("list_blogs.html", blogs=blogs)


@app.route("/blogs/update/<id>", methods=["GET", "POST"])
def update_note(id):
    """
    更新缺陷
    """
    if request.method == "GET":
        # 根据ID查询缺陷详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        # 渲染修改笔记页面HTML模板
        return rt("update_blog.html", blog=blog)
    else:
        # 获取请求的缺陷标题和正文
        line = request.form["line"]
        device_type = request.form["device_type"]
        device_part = request.form["device_part"]
        fault_content = request.form["fault_content"]
        fault_level = request.form["fault_level"]
        response = request.form["response"]

        # 更新缺陷
        blog = Blog.query.filter_by(id=id).update({"line": line, "device_type": device_type,
            "device_part": device_part, "fault_content": fault_content,
            "fault_level": fault_level,"response": response })
        # 提交才能生效
        db.session.commit()
        # 修改完成之后重定向到缺陷详情页面
        return redirect("/blogs/{id}".format(id=id))


@app.route("/blogs/<id>", methods=["GET", "DELETE"])
def query_note(id):
    """
    查询缺陷详情、删除缺陷
    """
    if request.method == "GET":
        # 到数据库查询缺陷详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        print(id, blog, "in query_blog", "@" * 20)
        # 渲染缺陷详情页面
        return rt("query_blog.html", blog=blog)
    else:
        # 删除缺陷
        blog = Blog.query.filter_by(id=id).delete()
        # 提交才能生效
        db.session.commit()
        # 返回204正常响应，否则页面ajax会报错
        return "", 204


### -------------end of home


### -------------start of profile


@app.route("/profile", methods=["GET", "DELETE"])
def query_profile():
    """
    查询缺陷详情、删除缺陷
    """

    id = session["userid"]

    if request.method == "GET":

        # 到数据库查询缺陷详情
        user = User.query.filter_by(id=id).first_or_404()
        print(user.username, user.password, "#" * 5)
        # 渲染缺陷详情页面
        return rt("profile.html", user=user)
    else:
        # 删除缺陷
        user = User.query.filter_by(id=id).delete()
        # 提交才能生效
        db.session.commit()
        # 返回204正常响应，否则页面ajax会报错
        return "", 204


@app.route("/profiles/update/<id>", methods=["GET", "POST"])
def update_profile(id):
    """
    更新缺陷
    """
    if request.method == "GET":
        # 根据ID查询缺陷详情
        user = User.query.filter_by(id=id).first_or_404()
        # 渲染修改笔记页面HTML模板
        return rt("update_profile.html", user=user)
    else:
        # 获取请求的缺陷标题和正文
        password = request.form["password"]
        nickname = request.form["nickname"]
        school_class = request.form["school_class"]
        school_grade = request.form["school_grade"]

        # 更新缺陷
        user = User.query.filter_by(id=id).update(
            {
                "password": password,
                "nickname": nickname,
                "school_class": school_class,
                "school_grade": school_grade,
            }
        )
        # 提交才能生效
        db.session.commit()
        # 修改完成之后重定向到缺陷详情页面
        return redirect("/profile")


### -------------end of profile


@app.route("/course/<id>", methods=["GET"])
def course_home(id):
    """
    查询缺陷详情、删除缺陷
    """
    if request.method == "GET":
        # 到数据库查询缺陷详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        teacherWork = TeacherWork.query.filter_by(course_id=id).first()
        print(id, blog, "in query_blog", "@" * 20)
        # 渲染缺陷详情页面
        return rt("course.html", blog=blog, teacherWork=teacherWork)
    else:
        return "", 204


login_manager = flask_login.LoginManager(app)
user_pass = {}


# @app.route("/call_bash", methods=["GET"])
# def call_bash():
#     i0bash_caller.open_client("")
#     return {}, 200


@app.route("/statistics", methods=["GET"])
def relationship():
    # static/data/test_data.json
    filename = os.path.join(app.static_folder, "data.json")
    with open(filename) as test_file:
        d = json.load(test_file)
    print(type(d), "#" * 10, d)
    return d


@login_manager.user_loader
def load_user(email):
    print("$" * 30)
    return user_pass.get(email, None)


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        data = User.query.filter_by(username=email, password=password).first()
        print(data, "@" * 10)
        if data is not None:
            print("test login")
            session["logged_in"] = True

            if email in admin_list:
                session["isadmin"] = True
            session["userid"] = data.id

            print("login sucess", "#" * 20, session["logged_in"])

            # w = TeacherWork.query.get(1)
            # print('w=', w, w.answer, w.title)
            # if w is not None:
            #     session['title'] = w.title
            #     session['detail'] = w.detail
            #     session['answer'] = w.answer

            return redirect(url_for("home", pagenum=1))
        else:
            return "Not Login"
    except Exception as e:
        print(e)
        return "Not Login"
    return redirect(url_for("home", pagenum=1))


@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    pw1 = request.form.get("password")
    pw2 = request.form.get("password2")
    if not pw1 == pw2:
        return redirect(url_for("home", pagenum=1))
    # if DB.get_user(email):
    if email in user_pass:
        print("already existed user")
        return redirect(url_for("home", pagenum=1))
    # salt = PH.get_salt()
    # hashed = PH.get_hash(pw1 + salt)
    print("register", email, pw1)
    new_user = User(username=email, password=pw1)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("home", pagenum=1))


@app.route("/logout")
def logout():
    session["logged_in"] = False
    return redirect(url_for("home", pagenum=1))


compare_results = []





@login_manager.unauthorized_handler
def unauthorized_handler():
    return "Unauthorized"


# --------------------------
# @app.route("/assignwork", methods=["GET"])
# def assignwork():
#     return rt("index.html")


# @app.route("/teacher_work", methods=["POST"])
# def teacher_work():

#     detail = request.form.get("detail")
#     print("#" * 20, detail, "@" * 20)
#     with open("movie/static/data.js", "w") as file:
#         file.write(detail)

#     return redirect(url_for("assignwork"))


@app.route("/student_work", methods=["POST"])
def student_work():
    return redirect(url_for("student_index"))


@app.route("/student_index", methods=["GET", "POST"])
def student_index():
    global compare_results
    print(len(compare_results), 'in student_index')
    return rt("student_index.html", compare_results=compare_results)


# @app.route("/", methods=["GET"])
# def index():
#     return rt("index.html")


@app.route("/file/upload", methods=["POST"])
def upload_part():  # 接收前端上传的一个分片
    task = request.form.get("task_id")  # 获取文件的唯一标识符
    chunk = request.form.get("chunk", 0)  # 获取该分片在所有分片中的序号
    filename = "%s%s" % (task, chunk)  # 构造该分片的唯一标识符
    print("filename=", filename)
    upload_file = request.files["file"]
    upload_file.save("./upload/%s" % filename)  # 保存分片到本地
    return rt("index.html")


@app.route("/file/merge", methods=["GET"])
def upload_success():  # 按序读出分片内容，并写入新文件
    global compare_results
    target_filename = request.args.get("filename")  # 获取上传文件的文件名
    task = request.args.get("task_id")  # 获取文件的唯一标识符
    chunk = 0  # 分片序号
    with open("./upload/%s" % target_filename, "wb") as target_file:  # 创建新文件
        while True:
            try:
                filename = "./upload/%s%d" % (task, chunk)
                source_file = open(filename, "rb")  # 按序打开每个分片
                target_file.write(source_file.read())  # 读取分片内容写入新文件
                source_file.close()
            except IOError as msg:
                break

            chunk += 1
            os.remove(filename)  # 删除该分片，节约空间

    # 上传成功，进行2个缺陷csv的比较的逻辑
    print('########################### start compare ###########################')
    # source = csv_reader('source_demo.csv')
    source = Blog.query.all()

    target = csv_reader('upload/'+target_filename)
    print(len(source), source[0], source[1])
    print('-'*20)
    print(len(target), target[0], target[1])
    for t in target:
        tname = t[3]
        for blog in source:
            sname = blog.fault_content
            c0 = jellyfish.levenshtein_distance(sname, tname)
            c1 = jellyfish.jaro_distance(sname, tname)
            c1 = round(c1, 4)
            c2 = jellyfish.damerau_levenshtein_distance(sname, tname)
            # https://en.wikipedia.org/wiki/Hamming_distance
            c3 = jellyfish.hamming_distance(sname, tname)
            print(c0, c1, c2, c3)
            # 我们可以更换所有模型，目前使用jaro_distance
            if c1 > 0.75:
                print('target=', tname, "#" * 10, 'most likely to be:', sname)
                compare_results.append([tname, sname, c1, blog.fault_level, blog.response])
    print('########################### end compare ###########################')
    # write_to_csv('results/results.csv', compare_results)
    return rt("student_index.html", compare_results=compare_results)


@app.route("/file/list", methods=["GET"])
def file_list():
    files = os.listdir("./results/")  # 获取文件目录
    # print(type(files))
    if ".DS_Store" in files:
        files.remove(".DS_Store")
    # files = map(lambda x: x if isinstance(x, unicode) else x.decode('utf-8'), files)  # 注意编码
    return rt("list.html", files=files)


@app.route("/file/download/<filename>", methods=["GET"])
def file_download(filename):
    def send_chunk():  # 流式读取
        store_path = "./results/%s" % filename
        print("store_path=", store_path)
        with open(store_path, "rb") as target_file:
            while True:
                chunk = target_file.read(20 * 1024 * 1024)
                if not chunk:
                    break
                yield chunk

    return Response(send_chunk(), content_type="application/octet-stream")


# Custom static data
# @app.route("/cdn/<path:filename>")
# def custom_static(filename):
#     print("#" * 20, filename, " in custom_static", app.root_path)
#     return send_from_directory(
#         "/Users/abel/Downloads/AbelProject/FlaskRepository/b13596campus_navigation/upload/",
#         filename,
#     )


# --------------------------


if __name__ == "__main__":
    db.create_all()

    app.run(host="localhost", port=5000, threaded=False)
