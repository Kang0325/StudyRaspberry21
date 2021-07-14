# index.html loading server

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', user='Kang', data={'userid':'noworry1', 'gender':'male', 'age':29})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)