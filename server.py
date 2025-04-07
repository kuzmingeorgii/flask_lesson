from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title=""):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8008)
