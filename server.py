from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


class MarsForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    education = StringField('Образование', validators=[DataRequired()])
    profession = StringField('Профессия', validators=[DataRequired()])
    sex = RadioField('Пол', choices=[('male', 'Мужской'), ('female', 'Женский')], validators=[DataRequired()])
    motivation = TextAreaField('Почему вы хотите участвовать в миссии?', validators=[DataRequired()])
    ready = BooleanField('Готовы остаться на Марсе?')
    submit = SubmitField('Отправить')


@app.route('/answer', methods=['GET', 'POST'])
def answer():
    form = MarsForm()
    if form.validate_on_submit():
        user_data = {
            'surname': form.surname.data,
            'name': form.name.data,
            'education': form.education.data,
            'profession': form.profession.data,
            'sex': form.sex.data,
            'motivation': form.motivation.data,
            'ready': form.ready.data,
        }
        return render_template('auto_answer.html', title='Ответ', user_data=user_data)
    return render_template('answer.html', title='Анкета', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8008)
