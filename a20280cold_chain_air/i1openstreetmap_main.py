"""App entry point."""
import os
import sys
import json

import math

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

# from flask import Flask

import folium
from folium import plugins
import numpy as np
from datetime import datetime
import random

# from weather import wheather_R

# print("#" * 20, wheather_R)
app = create_app()
app.secret_key = "ABCabc123"
app.debug = True
CORS(app)

# --- total requirement ----


# ---start  数据库 ---

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///campus_data.db"
db = SQLAlchemy(app)

# --- end   数据库 ---
admin_list = ["admin@126.com"]


def folim_create(start_coords, orginal=True):
    m = folium.Map(location=start_coords, width="100%", height="70%", zoom_start=14)

    # line_to_new_delhi = folium.PolyLine(
    #     [
    #         [46.67959447, 3.33984375],
    #         [46.5588603, 29.53125],
    #         [42.29356419, 51.328125],
    #         [35.74651226, 68.5546875],
    #         [28.65203063, 76.81640625],
    #     ]
    # ).add_to(m)
    tooltip = "click me to see more"

    ic0 = plugins.BeautifyIcon(
        border_color="#00ABDC",
        text_color="#00ABDC",
        number=0,
        inner_icon_style="margin-top:0;",
    )
    ic1 = plugins.BeautifyIcon(
        border_color="#00ABDC",
        text_color="#00ABDC",
        number=5,
        inner_icon_style="margin-top:0;",
    )
    ic2 = plugins.BeautifyIcon(
        border_color="#00ABDC",
        text_color="#00ABDC",
        number=5,
        inner_icon_style="margin-top:0;",
    )
    ic3 = plugins.BeautifyIcon(
        border_color="#00ABDC",
        text_color="#00ABDC",
        number=5,
        inner_icon_style="margin-top:0;",
    )
    ic4 = plugins.BeautifyIcon(
        border_color="#00ABDC",
        text_color="#00ABDC",
        number=5,
        inner_icon_style="margin-top:0;",
    )

    if orginal != True:
        # folium.Marker([51.5205898, -0.1424225], popup='ondon Central Hostel',tooltip=tooltip,icon=folium.Icon(color='red')).add_to(m)
        folium.Marker(
            [51.5205898, -0.1424225],
            popup="London Central Hostel",
            tooltip=tooltip,
            icon=ic0,
        ).add_to(m)
        folium.Marker(
            [51.503324, -0.119543],
            popup="Coca-Cola London Eye",
            tooltip=tooltip,
            icon=ic1,
        ).add_to(m)
        folium.Marker(
            [51.5138453, -0.0983506],
            popup="St. Paul's Cathedral",
            tooltip=tooltip,
            icon=ic2,
        ).add_to(m)
        folium.Marker(
            [51.5128019, -0.0834833],
            popup="Leadenhall Market",
            tooltip=tooltip,
            icon=ic3,
        ).add_to(m)
        folium.Marker(
            [51.508929, -0.128299],
            # [31.508929, 120.128299],
            popup="The National Gallery",
            tooltip=tooltip,
            icon=ic4,
        ).add_to(m)
        line_to_new_delhi = folium.PolyLine(
            [
                [51.5205898, -0.1424225],
                [51.503324, -0.119543],
                [51.5138453, -0.0983506],
                [51.5128019, -0.0834833],
                [51.508929, -0.128299],
            ],
            color="red",
        ).add_to(m)
        plugins.PolyLineTextPath(line_to_new_delhi, "London Tour", offset=-25).add_to(m)
    else:
        folium.Marker(
            [51.5205898, -0.1424225], popup="London Central Hostel", tooltip=tooltip
        ).add_to(m)
        folium.Marker(
            [51.503324, -0.119543], popup="Coca-Cola London Eye", tooltip=tooltip
        ).add_to(m)
        folium.Marker(
            [51.5138453, -0.0983506], popup="St. Paul's Cathedral", tooltip=tooltip
        ).add_to(m)
        folium.Marker(
            [51.5128019, -0.0834833], popup="Leadenhall Market", tooltip=tooltip
        ).add_to(m)
        folium.Marker(
            [51.508929, -0.128299], popup="The National Gallery", tooltip=tooltip
        ).add_to(m)
    # line_to_hanoi = folium.PolyLine(
    #     [
    #         [28.76765911, 77.60742188],
    #         [27.83907609, 88.72558594],
    #         [25.68113734, 97.3828125],
    #         [21.24842224, 105.77636719],
    #     ]
    # ).add_to(m)

    # plugins.PolyLineTextPath(line_to_hanoi, "To Hanoi", offset=-5).add_to(m)
    return m


"""
get from i3data_visualization

"""
fever_dict = {0: 3, 1: 640, 2: 322, 3: 52, 4: 1607}
"""
get from i3data_visualization and i2sentimanet_analys

"""
sentiment_dict = {
    0: [3, 0, 0],
    1: [202, 404, 101],
    2: [0, 303, 101],
    3: [0, 101, 0],
    4: [808, 606, 202],
}

additonal_information = [fever_dict, sentiment_dict]


def my_haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = (
        np.sin(delta_phi / 2) ** 2
        + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    )
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)


def hotness_sentiment_improve(base, vote):
    M = math.e * base * 100
    upper = 50
    down = 30
    a = M + math.log(math.e ** (vote / 2))
    b = M + math.log(math.e ** 1)

    r = a * 1.5 / b
    print("hotness_sentiment_improve a,b=", a, b, "result=", r)
    return r


def advanced_folim_create(start_coords, additonal_information=additonal_information):
    # global wheather_R
    fever_dict = additonal_information[0]
    sentiment_dict = additonal_information[1]

    total_km = []

    lat_logs = [
        [31.14, 121.29],
        [31.19, 120.37],
        [31.49, 120.37],
        [31.16, 120.10],
    ]
    places = [
        "订单1起点(上海市中心)",
        "订单1终点(苏州市附近）",
        "订单1实时位置",
        "订单2(杭州市附近）",
    ]
    # if not "rain" in wheather_R and not "snow" in wheather_R:
    for source in lat_logs:
        distances_km = []
        for row in lat_logs:
            distances_km.append(
                my_haversine_distance(source[0], source[1], row[0], row[1])
            )
        total_km.append(distances_km)
    print("total_km=", total_km)
    distances_sum = []
    for idx, val in enumerate(total_km):
        print(idx, sum(val))
        distances_sum.append(sum(val))
    print(distances_sum)
    new_values = []
    for i in range(0, len(distances_sum)):
        print(i)
        r = hotness_sentiment_improve(fever_dict[i], sentiment_dict[i][0])
        p = distances_sum[i] * r
        new_values.append(p)

    print("#" * 20, new_values)
    orders = np.argsort(new_values)
    print("order=", orders)
    sorted_places = np.array(lat_logs)[orders]
    sorted_placenames = places
    print("sorted_places=", sorted_places)
    print("sorted_placenames=", sorted_placenames)
    m = folium.Map(location=start_coords, width="100%", height="95%", zoom_start=8)

    # line_to_new_delhi = folium.PolyLine(
    #     [
    #         [46.67959447, 3.33984375],
    #         [46.5588603, 29.53125],
    #         [42.29356419, 51.328125],
    #         [35.74651226, 68.5546875],
    #         [28.65203063, 76.81640625],
    #     ]
    # ).add_to(m)
    tooltip = "click me to see more"

    ic0 = plugins.BeautifyIcon(
        border_color="#00ABDC",
        text_color="#00ABDC",
        number=0,
        inner_icon_style="margin-top:0;",
    )
    ic1 = plugins.BeautifyIcon(
        border_color="#00ABDC",
        text_color="#00ABDC",
        number=1,
        inner_icon_style="margin-top:0;",
    )
    ic2 = plugins.BeautifyIcon(
        border_color="#00ABDC",
        text_color="#00ABDC",
        number=2,
        inner_icon_style="margin-top:0;",
    )
    ic3 = plugins.BeautifyIcon(
        border_color="#00ABDC",
        text_color="#00ABDC",
        number=3,
        inner_icon_style="margin-top:0;",
    )
    ic4 = plugins.BeautifyIcon(
        border_color="#00ABDC",
        text_color="#00ABDC",
        number=4,
        inner_icon_style="margin-top:0;",
    )

    index = 0
    for p, name in zip(sorted_places, sorted_placenames):
        print(p[0], p[1], "#" * 10, name)
        myic = plugins.BeautifyIcon(
            border_color="#00ABDC",
            text_color="#00ABDC",
            number=index,
            inner_icon_style="margin-top:0;",
        )
        # folium.Marker([51.5205898, -0.1424225], popup='ondon Central Hostel',tooltip=tooltip,icon=folium.Icon(color='red')).add_to(m)
        popup = folium.Popup(f"<h5>{name}</h5>", max_width=300, min_width=300)
        folium.Marker([p[0], p[1]], popup=popup, tooltip=tooltip, icon=myic).add_to(m)
        index += 1
    # folium.Marker([51.503324, -0.119543], popup='Coca-Cola London Eye',tooltip=tooltip,icon=ic1).add_to(m)
    # folium.Marker([51.5138453, -0.0983506], popup="St. Paul's Cathedral",tooltip=tooltip,icon=ic2).add_to(m)
    # folium.Marker([51.5128019, -0.0834833], popup='Leadenhall Market',tooltip=tooltip,icon=ic3).add_to(m)
    # folium.Marker([51.508929 , -0.128299], popup='The National Gallery',tooltip=tooltip,icon=ic4).add_to(m)
    # line_to_new_delhi = folium.PolyLine(sorted_places, color="red").add_to(m)
    # plugins.PolyLineTextPath(line_to_new_delhi, "London Tour", offset=-25).add_to(m)

    # line_to_hanoi = folium.PolyLine(
    #     [
    #         [28.76765911, 77.60742188],
    #         [27.83907609, 88.72558594],
    #         [25.68113734, 97.3828125],
    #         [21.24842224, 105.77636719],
    #     ]
    # ).add_to(m)

    # plugins.PolyLineTextPath(line_to_hanoi, "To Hanoi", offset=-5).add_to(m)
    return m


@app.route("/orginal")
def orginal():
    start_coords = (51.5205898, -0.1424225)
    # folium_map = folium.Map(location=start_coords, zoom_start=14)
    folium_map = folim_create(start_coords, orginal=True)
    return folium_map._repr_html_()


@app.route("/path")
def index():
    start_coords = (51.503324, -0.119543)
    # folium_map = folium.Map(location=start_coords, zoom_start=14)
    folium_map = folim_create(start_coords, orginal=False)
    return folium_map._repr_html_()


@app.route("/advanced_path")
def advance_path():
    start_coords = (31.50000, 121.43333)
    # folium_map = folium.Map(location=start_coords, zoom_start=14)
    folium_map = advanced_folim_create(start_coords, additonal_information)
    return folium_map._repr_html_()


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
    订单数据模型
    """

    # 主键ID
    id = db.Column(db.Integer, primary_key=True)
    # 订单标题
    title = db.Column(db.String(100))
    # 订单正文
    text = db.Column(db.Text)
    # 入库时间
    start_time = db.Column(db.String(100))
    #  出库时间
    end_time = db.Column(db.String(100))
    # 地点
    start_place = db.Column(db.String(100))
    end_place = db.Column(db.String(100))

    def __init__(self, title, text, start_time, end_time, start_place, end_place):
        """
        初始化方法
        """
        self.title = title
        self.text = text
        self.start_time = start_time
        self.end_time = end_time
        self.start_place = start_place
        self.end_place = end_place


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
    def __init__(self, data, page=1, number=10):
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
            for blog in blogs:
                if keyword in blog.title or keyword in blog.text:
                    blog.title = replace_html_tag(blog.title, keyword)
                    print(blog.title)
                    blog.text = replace_html_tag(blog.text, keyword)

                    search_list.append(blog)

            if len(search_list) == 0 and keyword in ['天气', '心情']:
                es_content = es_search.mysearch(keyword)
                search_list.append(es_content)
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
        return rt("home.html", listing=PageResult(search_list, pagenum, 10), user=user, keyword=keyword)

    return rt("home.html", listing=PageResult(blogs, pagenum), user=user)


@app.route("/blogs/create", methods=["GET", "POST"])
def create_blog():
    """
    创建订单item
    """
    if request.method == "GET":
        # 如果是GET请求，则渲染创建页面
        return rt("create_blog.html")
    else:
        # 从表单请求体中获取请求数据
        title = request.form["title"]
        text = request.form["text"]

        start_time = request.form["start_time"]
        end_time = request.form["end_time"]
        start_place = request.form["start_place"]
        end_place = request.form["end_place"]

        # 创建一个订单对象
        blog = Blog(
            title=title,
            text=text,
            start_time=start_time,
            end_time=end_time,
            start_place=start_place,
            end_place=end_place,
        )
        db.session.add(blog)
        # 必须提交才能生效
        db.session.commit()
        # 创建完成之后重定向到订单列表页面
        return redirect("/blogs")


@app.route("/blogs", methods=["GET"])
def list_notes():
    """
    查询订单列表
    """
    blogs = Blog.query.all()
    # 渲染订单列表页面目标文件，传入blogs参数
    return rt("list_blogs.html", blogs=blogs)


@app.route("/blogs/update/<id>", methods=["GET", "POST"])
def update_note(id):
    """
    更新订单
    """
    if request.method == "GET":
        # 根据ID查询订单详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        # 渲染修改笔记页面HTML模板

        return rt("update_blog.html", blog=blog)
    else:
        # 获取请求的订单标题和正文
        title = request.form["title"]
        text = request.form["text"]

        # 更新订单
        blog = Blog.query.filter_by(id=id).update({"title": title, "text": text})
        # 提交才能生效
        db.session.commit()
        # 修改完成之后重定向到订单详情页面
        return redirect("/blogs/{id}".format(id=id))


def time_trans(x):
    print("x=", x)
    if "年" not in x:
        x = "2022年" + x
    year = x.split("年")[0]
    month = x.split("年")[1].split("月")[0]
    day = x.split("年")[1].split("月")[1].split("日")[0]
    print("y", year, "m=", month, "d=", day)
    if len(day) >= 3:
        day = day[0] + day[2]

    # chinese_english = dict(零=0,一=1,二=2,三=3,四=4,五=5,六=6,七=7,八=8,九=9,十=10)
    # year = "".join(str(chinese_english[i]) for i in year)
    # month = "".join(str(chinese_english[i]) for i in month)
    # day = "".join(str(chinese_english[i]) for i in day)
    if len(month) == 3:
        month = month[0] + month[2]
    if len(day) == 3:
        day = day[0] + day[2]
    final_date = year + "-" + month + "-" + day + " 00:00:00"
    return final_date


@app.route("/blogs/<id>", methods=["GET", "DELETE"])
def query_note(id):

    """
    查询订单详情、删除订单
    """
    if request.method == "GET":
        # 到数据库查询订单详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        print(id, blog, "in query_blog", "@" * 20)
        # 渲染订单详情页面

        # 从预测模型得到
        parameters = [0.09633556, 0.25799959, 0.11092464, -0.12864146]

        now = datetime.now()
        h = None
        if blog.start_time is not None:
            h = datetime_object = datetime.strptime(
                time_trans(blog.start_time), "%Y-%m-%d %H:%M:%S"
            )
        else:
            h = datetime.datetime(1970, 1, 1)
        duration = now - h
        total = round(duration.total_seconds() / 60 * 24 * 60)
        r = (
            parameters[0] * total ** 3
            + parameters[1] * total ** 2
            + parameters[2] * total
            + parameters[3]
        )
        myr = random.randint(0, blog.id)
        r = pow(r, 1 / 8) + myr
        print(total, "#" * 10, r, "#" * 30)

        return rt("query_blog.html", blog=blog, predict=round(r, 2))
    else:
        # 删除订单
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
    查询订单详情、删除订单
    """

    id = session["userid"]

    if request.method == "GET":

        # 到数据库查询订单详情
        user = User.query.filter_by(id=id).first_or_404()
        print(user.username, user.password, "#" * 5)
        # 渲染订单详情页面
        return rt("profile.html", user=user)
    else:
        # 删除订单
        user = User.query.filter_by(id=id).delete()
        # 提交才能生效
        db.session.commit()
        # 返回204正常响应，否则页面ajax会报错
        return "", 204


@app.route("/profiles/update/<id>", methods=["GET", "POST"])
def update_profile(id):
    """
    更新订单
    """
    if request.method == "GET":
        # 根据ID查询订单详情
        user = User.query.filter_by(id=id).first_or_404()
        # 渲染修改笔记页面HTML模板
        return rt("update_profile.html", user=user)
    else:
        # 获取请求的订单标题和正文
        password = request.form["password"]
        nickname = request.form["nickname"]
        school_class = request.form["school_class"]
        school_grade = request.form["school_grade"]

        # 更新订单
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
        # 修改完成之后重定向到订单详情页面
        return redirect("/profile")


### -------------end of profile


@app.route("/course/<id>", methods=["GET"])
def course_home(id):
    """
    查询订单详情、删除订单
    """
    if request.method == "GET":
        # 到数据库查询订单详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        teacherWork = TeacherWork.query.filter_by(course_id=id).first()
        print(id, blog, "in query_blog", "@" * 20)
        # 渲染订单详情页面
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


reviews = []


@login_manager.unauthorized_handler
def unauthorized_handler():
    return "Unauthorized"


# --------------------------


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

    return rt("index.html")


@app.route("/file/list", methods=["GET"])
def file_list():
    files = os.listdir("./upload/")  # 获取文件目录
    # print(type(files))
    files.remove(".DS_Store")
    # files = map(lambda x: x if isinstance(x, unicode) else x.decode('utf-8'), files)  # 注意编码
    return rt("list.html", files=files)


@app.route("/file/download/<filename>", methods=["GET"])
def file_download(filename):
    def send_chunk():  # 流式读取
        store_path = "./upload/%s" % filename
        print("store_path=", store_path)
        with open(store_path, "rb") as target_file:
            while True:
                chunk = target_file.read(20 * 1024 * 1024)
                if not chunk:
                    break
                yield chunk

    return Response(send_chunk(), content_type="application/octet-stream")


# Custom static data
@app.route("/cdn/<path:filename>")
def custom_static(filename):
    print("#" * 20, filename, " in custom_static", app.root_path)
    return send_from_directory(
        "/Users/abel/Downloads/AbelProject/FlaskRepository/b13596campus_navigation/upload/",
        filename,
    )


# --------------------------


if __name__ == "__main__":
    db.create_all()

    app.run(host="localhost", port=5000, threaded=False)
