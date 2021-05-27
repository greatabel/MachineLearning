#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request,Blueprint
from flask import render_template
from flask import make_response

from flask_docs import ApiDoc


from predict_realdata import flow_predict
from process_phone_with_transaction import load_obj


app = Flask(__name__)
app.debug = True


#-- 需要显示文档的 Api --
app.config["API_DOC_MEMBER"] = ["api", "platform"]

ApiDoc(app, title="Sample App", version="1.0.0")

api = Blueprint("api", __name__)
platform = Blueprint("platform", __name__)

# http://127.0.0.1:5000/docs/api/
#--  结束文档设置 --


@api.route("/predict/")
@api.route("/predict/<index_id>")
def scp2(index_id=""):
    """predict get
    @@@
    ### args
    |  comment |
    |-------|----------|--------------|------|----------|
    | phonenumber or deviceid
    ### request
    ```json
    {"comment": "13971113343"} or {'comment': 'deviceid001'}
    ```
    ### return
    ```json
    {"query_value":query_value,  'k_v':k_v}
    ```
    """
    k_v = load_obj("k_v")
    index = ""

    query_value = request.args.get("comment")
    print("comment=", query_value)
    if query_value != None:

        result = flow_predict(query_value)
        index = str(result) + " !!!"
    r = make_response(
        render_template("scp2.html", query_value=query_value, index=index, k_v=k_v)
    )

    return r


if __name__ == "__main__":
    """
    启动主程序功能
    """
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(platform, url_prefix="/platform")
    app.run()
