from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title=""):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    is_engineer = 'инженер' in prof.lower() or 'строитель' in prof.lower()

    title = "Инженерные тренажеры" if is_engineer else "Научные симуляторы"
    image = "engineer.jpg" if is_engineer else "scientist.jpg"

    return render_template('training.html', title=title, image=image)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8008)
