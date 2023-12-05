from flask import Flask,jsonify,render_template_string,request,Response,render_template, send_from_directory
import subprocess, os
from werkzeug.datastructures import Headers
from werkzeug.utils import secure_filename
import sqlite3


app = Flask(__name__)
app.config['UPLOAD_FOLDER']="/home/kali/Desktop/upload"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route('/')
def home():
    return "<h1>Vulnerable app</h1>"

#xss
@app.route("/xss")
def index():
    name = request.args.get('name', '')
    return f"Hello, {name}!"

#idor
data = {
    '1': 'Vania',
    '2': 'Jacob',
    '3': 'Alex'
}
@app.route('/users')
def get_user():
    user_id = request.args.get('id')
    if user_id in data:
        return f"User: {data[user_id]}"
    else:
        return "User not found"

#sqli
@app.route("/user/<string:name>")
def search_user(name):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    cur.execute("select * from test where username = '%s'" % name)
    data = str(cur.fetchall())
    con.close()
    import logging
    logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
    logging.debug(data)
    return jsonify(data=data),200

#OS injection
@app.route("/os_inj")
def page():
    cmd = request.args.get("hostname")
    return subprocess.check_output(cmd, shell=True)

#Path traversal
@app.route("/read_file")
def read_file():
    filename = request.args.get('filename')
    file = open(filename, "r")
    data = file.read()
    file.close()
    return jsonify(data=data),200

#Brute force
@app.route('/login',methods=["GET"])
def login():
    username=request.args.get("username")
    passwd=request.args.get("password")
    if "admin" in username and "superadmin" in passwd:
        return jsonify(data="Login successful"), 200
    else:
        return jsonify(data="Login unsuccessful"), 403


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8081)
