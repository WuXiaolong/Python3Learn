# wxl_flask.py
from flask import Flask, jsonify, abort
from wxl_pymysql import *

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, Flask!"
    # return jsonify({'data': query_table(), 'code': 200})


@app.route('/developer/api/v1.0/all', methods=['GET'])
def get_all():
    return jsonify({'data': query_table(), 'code': 200})


@app.route('/developer/api/v1.0/all/<int:id>', methods=['GET'])
def get_developer(id):
    # result = [task for task in tasks if task_id == task['id']]
    result = query_table_id(id)
    if len(result) == 0:
        abort(404)
    return jsonify({'data': result})


@app.route('/developer/api/v1.0/insert', methods=['POST'])
def insert_task():
    result = insert_table()
    print(result)
    return jsonify({'code': 200})


@app.route('/developer/api/v1.0/update', methods=['PUT'])
def update_task():
    result = update_table()
    print(result)
    return jsonify({'code': 200})


@app.route('/developer/api/v1.0/delete', methods=['DELETE'])
def delete_task():
    result = delete_table()
    print(result)
    return jsonify({'code': 200})


if __name__ == '__main__':
    app.run(debug=True)  # 使用 flask 自带的服务器
