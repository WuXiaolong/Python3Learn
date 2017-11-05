# wxl_flask.py
from flask import Flask, jsonify, abort, request
from wxl_pymysql import *

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, Flask!"


# get 方式
@app.route('/developer/api/v1.0/all', methods=['GET'])
def get_all():
    print(request.headers)
    print('request.method=' + request.method)
    # var = request.headers['Application-Id':123456]
    return jsonify({'data': query_table(), 'code': 200})


# get 方式，带参
@app.route('/developer/api/v1.0/all/<int:developer_id>', methods=['GET'])
def get_developer(developer_id):
    result = query_table_id(developer_id)
    if len(result) == 0:
        abort(404)
    return jsonify({'data': result})


# post 方式
@app.route('/developer/api/v1.0/insert', methods=['POST'])
def insert_task():
    result = insert_table()
    print(result)
    return jsonify({'code': 200})


# put 方式
@app.route('/developer/api/v1.0/update', methods=['PUT'])
def update_task():
    result = update_table()
    print(result)
    return jsonify({'code': 200})


# delete 方式
@app.route('/developer/api/v1.0/delete', methods=['DELETE'])
def delete_task():
    result = delete_table()
    print(result)
    return jsonify({'code': 200})


if __name__ == '__main__':
    app.run(port=1024, debug=True)  # 端口1024，调试模式，使用 flask 自带的服务器
