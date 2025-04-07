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


@app.route('/ol/<list_type>')
def list_prof(list_type):
    professions = [
        "инженер-исследователь", "пилот", "строитель", "экзобиолог",
        "врач", "инженер по терраформированию", "климатолог",
        "специалист по радиационной защите", "астрогеолог", "гляциолог",
        "инженер жизнеобеспечения", "метеоролог", "оператор марсохода",
        "киберинженер", "штурман", "пилот дронов"
    ]

    if list_type not in ['ol', 'ul']:
        list_type = None

    return render_template('list_prof.html', list_type=list_type, professions=professions)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8008)
