import json
import os
import time

from flask import Flask, request, make_response, jsonify, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
user_token_dic = {
    'user01': '3b6754f00bb0063071c5b71ce2b56b4ed0ce56a63493e785bea85b74c41ce200'
    , 'user02': 'dcdc7286f6822dc5a4b54d2ce53f40ae0e562d7fc06d64b8dd332f7d528c7c67'
    , 'user03': '04c4fba92b3451b16daedbbc7dd4cec84b8a88333f3da60626c6abbfdc829a02'
    , 'user04': '3c3a7fa64c34e2530b708ec9bdeedd49e0098bfd3239b1cd58985feeb38531b8'
    , 'user05': 'abb9d47918055902a8a6f3f8e86cd962d37d49647e9b51bdd7f7d67ff95f9864'
    , 'user06': '6b2b8f34dd4ad1812a76a7037ed23d9ebc0189070320fa32dc610a79852419c7'
    , 'user07': 'aac287a1eeb39d1983aaa732a7a5f33a64918adb1e88da6b344d2090eaed7239'
    , 'user08': '3d0c7ff2ad3063bc0e93befeef895def90290114ee590ca09b60f8e4476aca27'
    , 'user09': 'a0a9941e29cebdd732a2a57411f14d45e14bc3061d66c2e1c30eca421ed0b02d'
    , 'user10': '34467677a88fc7966807c26ced0972cc775be9e6983d4bfbd2a0981a4350dcfd'
}
menu_json = {
    "code": "200",
    "breakfast": [
        {
            "menu_nunber": "01",
            "menu_price": 5.50,
            "menu_name": "小笼包"
        },
        {
            "menu_nunber": "02",
            "menu_price": 3.00,
            "menu_name": "八宝粥"
        },
        {
            "menu_nunber": "03",
            "menu_price": 1.50,
            "menu_name": "油条"
        },
        {
            "menu_nunber": "04",
            "menu_price": 1.00,
            "menu_name": "茶叶蛋"
        },
        {
            "menu_nunber": "05",
            "menu_price": 1.50,
            "menu_name": "豆包"
        },
        {
            "menu_nunber": "06",
            "menu_price": 2.00,
            "menu_name": "烧饼"
        }
    ],
    "lunch": [
        {
            "menu_nunber": "07",
            "menu_price": 17.00,
            "menu_name": "宫保鸡丁"
        },
        {
            "menu_nunber": "08",
            "menu_price": 25.00,
            "menu_name": "锅包肉"
        },
        {
            "menu_nunber": "09",
            "menu_price": 35.00,
            "menu_name": "糖醋排骨"
        },
        {
            "menu_nunber": "10",
            "menu_price": 30.00,
            "menu_name": "蒜台炒肉片"
        },
        {
            "menu_nunber": "11",
            "menu_price": 25.50,
            "menu_name": "酸辣土豆丝"
        },
        {
            "menu_nunber": "12",
            "menu_price": 32.00,
            "menu_name": "红烧茄子"
        }
    ],
    "dinner": [
        {
            "menu_nunber": "13",
            "menu_price": 21.00,
            "menu_name": "辣椒炒肉"
        },
        {
            "menu_nunber": "14",
            "menu_price": 15.00,
            "menu_name": "豌豆肉片汤"
        },
        {
            "menu_nunber": "15",
            "menu_price": 26.00,
            "menu_name": "原味五花肉卷"
        },
        {
            "menu_nunber": "16",
            "menu_price": 20.00,
            "menu_name": "醋溜白菜"
        },
        {
            "menu_nunber": "17",
            "menu_price": 25.50,
            "menu_name": "地三鲜"
        },
        {
            "menu_nunber": "18",
            "menu_price": 39.00,
            "menu_name": "红烧排骨"
        }
    ]
}

server_internal_error_data = {
    "code": "500",
    "message": "Server internal error."
}

UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF', 'doc', 'docx', 'ppt', 'pptx'])


@app.route("/api/v1/user/login", methods=['POST'])
def login():
    """登录接口，输入参数格式：
        "authRequest": {
            "userName": "[username]",
            "password": "[password]"
        }

        :return
        Success : http code 200
        {
            "code": "200",
            "message": "login success",
            "access_token": "3b6754f00bb0063071c5b71ce2b56b4ed0ce56a63493e785bea85b74c41ce200"
        }

        Fail : http code 401
        {
            "code": "401",
            "message": "login fail"
        }
    """
    try:
        raw_data = request.get_data(as_text=True)
        data = json.loads(raw_data)
        username = data.get("authRequest").get("userName")
        password = data.get("authRequest").get("password")

        if username not in user_token_dic.keys() or password != 'pwd':
            print('Username or password error!')
            login_fail_resp_data = {
                "code": "401",
                "message": "login fail"
            }
            return make_response(jsonify(login_fail_resp_data), '401')

        login_succ_resp_data = {
            "code": "200",
            "message": "login success",
            "access_token": user_token_dic.get(username)
        }

        return make_response(jsonify(login_succ_resp_data), '200')
    except Exception:
        return make_response(jsonify(server_internal_error_data), '500')


@app.route('/api/v1/menu/list', methods=['GET'])
def list():
    """菜单浏览接口

    :return: 菜单列表
    """
    access_token = request.headers.get("access_token")

    if access_token is None:
        login_fail_resp_data = {
            "code": "401",
            "message": "Please login first."
        }
        return make_response(jsonify(login_fail_resp_data), '401')

    if access_token not in user_token_dic.values():
        print('access_token error, please re-login.')
        login_fail_resp_data = {
            "code": "401",
            "message": "Unknown user info, please re-login."
        }
        return make_response(jsonify(login_fail_resp_data), '401')

    category = request.args.get("type")

    if category is not None:
        return make_response(jsonify(menu_json.get(category)), 200)

    return make_response(jsonify(menu_json), 200)


@app.route("/api/v1/menu/confirm", methods=['POST'])
def confirm():
    """下单接口，输入参数格式：
        header = {'access_token' : ''}
        data:
        {
            "order_list": [
                {
                    "menu_nunber" : "01",
                    "number" : 1
                },
                {
                    "menu_nunber" : "03",
                    "number" : 2
                },
                {
                    "menu_nunber" : "04",
                    "number" : 1
                },
                {
                    "menu_nunber" : "05",
                    "number" : 3
                }
            ]
        }

        :return
        Success : http code 200
        {
            "code": "200",
            "message": "Order success.",
            "total": 7
        }

        not login : http code 401
        {
            "code": "401",
            "message": "Please login first."
        }
    """
    try:
        access_token = request.headers.get("access_token")
        if access_token is None:
            login_fail_resp_data = {
                "code": "401",
                "message": "Please login first."
            }
            return make_response(jsonify(login_fail_resp_data), '401')

        raw_data = request.get_data(as_text=True)
        order_list = json.loads(raw_data).get("order_list")
        total = 0
        for order in order_list:
            total = total + order.get("number")
            time.sleep(0.6)

        order_success_resp_data = {
            "code": "200",
            "message": "Order success.",
            "total": total
        }
        return make_response(jsonify(order_success_resp_data), '200')
    except Exception:
        return make_response(jsonify(server_internal_error_data), '500')


@app.route("/api/v1/user/logout", methods=['DELETE'])
def logout():
    """用户注销接口，输入参数格式：
        header = {'access_token' : ''}
    """
    try:
        access_token = request.headers.get("access_token")

        if access_token not in user_token_dic.values():
            print('access_token error, logout failed.')
            login_fail_resp_data = {
                "code": "401",
                "message": "Unknown user info, logout fail."
            }
            return make_response(jsonify(login_fail_resp_data), '401')

        login_succ_resp_data = {
            "code": "200",
            "message": "logout success"
        }

        return make_response(jsonify(login_succ_resp_data), '200')
    except Exception:
        return make_response(jsonify(server_internal_error_data), '500')


# suffix validation
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# upload file testing page
@app.route('/', methods=['GET'], strict_slashes=False)
def indexpage():
    return render_template('index.html')


# upload file
@app.route('/uploadfile', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['file']  # get the file name

    if f and allowed_file(f.filename):  # Verify the file type
        fname = secure_filename(f.filename)
        ext = fname.rsplit('.', 1)[1]
        unix_time = time.time()
        new_filename = str(unix_time) + '.' + ext
        f.save(os.path.join(file_dir, new_filename))
        print(f'{f.filename} upload success!')
        return jsonify({'code': 200, 'result': 'success', 'msg': f'file {f.filename} upload success'})
    else:
        print(f'{f.filename} upload failed!')
        return jsonify(
            {'code': 500, 'result': 'failed', 'msg': f'file {f.filename} upload fail, please check the file type'})


if __name__ == "__main__":
    app.run(port=9091, debug=True, host='0.0.0.0')

    # Demo for https, password = 1234
    # app.run('0.0.0.0', debug=True, port=8100, ssl_context=(f'{os.path.abspath(os.curdir)}/cert_files/server.crt'
    #                                                        , f'{os.path.abspath(os.curdir)}/cert_files/server.key'))
