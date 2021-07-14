# index.html loading server
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/post', methods=['POST'])
def post():
    userid = request.form.get('userid')
    password = request.form.get('password')
    msg = "{0} / {1}".format(userid, password)
    return msg

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)