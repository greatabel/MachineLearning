"""App entry point."""
import os
import sys
import json
import random
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
from flask import make_response

# from flask_wtf.csrf import CSRFProtect
from flask import flash

from movie import create_app

# import es_search
import logging
import numpy as np
from scipy.integrate import odeint
import pandas as pd
import plotly.express as px
from flask import  render_template_string


app = create_app()
app.secret_key = "ABCabc123"
app.debug = True


handler = logging.FileHandler("flask.log", encoding="UTF-8")
handler.setLevel(
    logging.DEBUG
)  # 设置日志记录最低级别为DEBUG，低于DEBUG级别的日志记录会被忽略，不设置setLevel()则默认为NOTSET级别。
logging_format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s"
)
handler.setFormatter(logging_format)
app.logger.addHandler(handler)


CORS(app)

# 防御点3: CSRF攻击模拟 防御
# CSRFProtect(app)

# --- total requirement ----


# ---start  数据库 ---

print("#" * 20, os.path.abspath("movie/campus_data.db"), "#" * 20)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(
    "movie/campus_data.db"
)
# 防御点1: 防止入sql-inject ，不实用sql注入，sqlchemy让代码ORM化，安全执行
db = SQLAlchemy(app)

last_upload_filename = None
# --- end   database  ---
admin_list = ["admin@126.com", "greatabel1@126.com"]


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
    ppt entity
    """


    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))

    text = db.Column(db.Text)

    def __init__(self, title, text):
        """
        初始化方法
        """
        self.title = title
        self.text = text


### -------------start of home
def replace_html_tag(text, word):
    new_word = '<font color="red">' + word + "</font>"
    len_w = len(word)
    len_t = len(text)
    for i in range(len_t - len_w, -1, -1):
        if text[i : i + len_w] == word:
            text = text[:i] + new_word + text[i + len_w :]
    return text


class PageResult:
    def __init__(self, data, page=1, number=4):
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


@app.route("/plot_demand/<string:material>")
def plot_demand(material):
    material = material.lower()
    if material == "aggregate":
        file_path = "data/Aggregate/predictions_2023.csv"
        title = "Demand Prediction for 2023 (Aggregate)"
    elif material == "concrete":
        file_path = "data/Concrete/predictions_2023.csv"
        title = "Demand Prediction for 2023 (Concrete)"
    else:
        return "Invalid material. Please choose 'aggregate' or 'concrete'."

    # 从CSV文件读取预测数据
    predictions_2023_df = pd.read_csv(file_path)

    # 使用Plotly创建交互式折线图
    fig = px.line(predictions_2023_df, x='timestamp', y='prediction', title=title)

    # 将图形转换为HTML
    plot_html = fig.to_html(full_html=False)

    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
            {plot_html}
        </body>
    </html>
    """)




@app.route("/home/<int:pagenum>", methods=["GET"])
@app.route("/home", methods=["GET", "POST"])
def home(pagenum=1):
    print("home " * 10)
    app.logger.info("home info log")

    blogs = Blog.query.all()
    blogs = list(reversed(blogs))
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
            for blog in blogs:
                if keyword in blog.title or keyword in blog.text:
                    blog.title = replace_html_tag(blog.title, keyword)
                    print(blog.title)
                    blog.text = replace_html_tag(blog.text, keyword)

                    search_list.append(blog)

            # if len(search_list) == 0 and keyword in ["天气", "心情"]:
            #     es_content = es_search.mysearch(keyword)
            #     search_list.append(es_content)
            # for movie in notice_list:
            #     if movie.director.director_full_name == keyword:
            #         search_list.append(movie)

            #     for actor in movie.actors:
            #         if actor.actor_full_name == keyword:
            #             search_list.append(movie)
            #             break

            #     for gene in movie.genres:
            #         if gene.genre_name == keyword:
            #             search_list.append(movie)
            #             break
        print("search_list=", search_list, "=>" * 5)
        return rt(
            "home.html",
            listing=PageResult(search_list, pagenum, 10),
            user=user,
            keyword=keyword,
        )
        # return rt("home.html", listing=PageResult(search_list, pagenum, 2), user=user)

    return rt("home.html", listing=PageResult(blogs, pagenum), user=user)


@app.route("/blogs/create", methods=["GET", "POST"])
def create_blog():
    """
    创建ppt文章
    """
    if request.method == "GET":
        # 如果是GET请求，则渲染创建页面
        return rt("create_blog.html")
    else:
        # 从表单请求体中获取请求数据
        title = request.form["title"]
        text = request.form["text"]

        # 创建一个ppt对象
        blog = Blog(title=title, text=text)
        db.session.add(blog)
        # 必须提交才能生效
        db.session.commit()
        # 创建完成之后重定向到ppt列表页面
        return redirect("/blogs")


@app.route("/blogs", methods=["GET"])
def list_notes():
    """
    查询ppt列表
    """
    blogs = Blog.query.all()

    # 渲染ppt列表页面目标文件，传入blogs参数
    return rt("list_blogs.html", blogs=blogs)


@app.route("/blogs/update/<id>", methods=["GET", "POST"])
def update_note(id):
    """
    更新Predict_Category
    """
    if request.method == "GET":
        # 根据ID查询ppt详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        # 渲染修改笔记页面HTML模板
        return rt("update_blog.html", blog=blog)
    else:
        # 获取请求的ppt标题和正文
        title = request.form["title"]
        text = request.form["text"]

        # 更新ppt
        blog = Blog.query.filter_by(id=id).update({"title": title, "text": text})
        # 提交才能生效
        db.session.commit()
        # 修改完成之后重定向到ppt详情页面
        return redirect("/blogs/{id}".format(id=id))


@app.route("/blogs/<id>", methods=["GET", "DELETE"])
def query_note(id):
    """
    查询Predict_Category详情、删除Predict_Category
    """
    if request.method == "GET":
        # 到数据库查询ppt详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        print(id, blog, "in query_blog", "@" * 20)
        # 渲染ppt详情页面
        return rt("query_blog.html", blog=blog)
    else:
        # 删除ppt
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
    查询Predict_Category详情、删除ppt
    """

    id = session["userid"]

    if request.method == "GET":

        # 到数据库查询ppt详情
        user = User.query.filter_by(id=id).first_or_404()
        print(user.username, user.password, "#" * 5)
        # 渲染ppt详情页面
        r = make_response(rt("profile.html", user=user))
        # 防御点2：xss攻击，实用csp方式： https://content-security-policy.com/
        r.headers.set(
            "Content-Security-Policy",
            "default-src * 'unsafe-inline'; connect-src 'self' 'nonce-987654321' ",
        )
        return r
    else:
        # 删除ppt
        user = User.query.filter_by(id=id).delete()
        # 提交才能生效
        db.session.commit()
        # 返回204正常响应，否则页面ajax会报错
        return "", 204


@app.route("/profiles/update/<id>", methods=["GET", "POST"])
def update_profile(id):
    """
    更新ppt
    """
    if request.method == "GET":
        # 根据ID查询ppt详情
        user = User.query.filter_by(id=id).first_or_404()
        # 渲染修改笔记页面HTML模板
        return rt("update_profile.html", user=user)
    else:
        # 获取请求的ppt标题和正文
        password = request.form["password"]
        nickname = request.form["nickname"]
        school_class = request.form["school_class"]
        school_grade = request.form["school_grade"]

        # 更新ppt
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
        # 修改完成之后重定向到ppt详情页面
        return redirect("/profile")


### -------------end of profile




login_manager = flask_login.LoginManager(app)
user_pass = {}


# @app.route("/call_bash", methods=["GET"])
# def call_bash():
#     i0bash_caller.open_client("")
#     return {}, 200


@app.route("/statistics", methods=["GET"])
def relationship():
    # 加载哪个刺绣的知识图谱
    queryid = request.args.get("id")

    if queryid is not None:
        print("-" * 20)
        print("##kg want queryid=", queryid, "#" * 30)

        # static/data/test_data.json
        filename = os.path.join(app.static_folder, "kg_data/" + queryid + ".json")
        if os.path.isfile(filename):
            print(filename, " ## It is a file")
    else:
        filename = os.path.join(app.static_folder, "kg_data/default.json")
        print(filename, " ## use default file")

    # with open(filename) as test_file:
    with open(filename, "r", encoding="utf-8") as test_file:
        d = json.load(test_file)
    print(type(d), "#" * 10, d)
    return jsonify(d)





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
                print("@" * 20, "setting isadmin")
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
    data = User.query.filter_by(username=email).first()
    # if email in user_pass:
    if data is not None:
        print("already existed user")
        flash("already existed user")
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


reviews = []


@login_manager.unauthorized_handler
def unauthorized_handler():
    return "Unauthorized"







# --------------------------


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        app.run(host="localhost", port=5000, threaded=False)
