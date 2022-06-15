from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class HeadHunterForm(FlaskForm):
    search_bar = StringField('Введите строку поиска', validators=[DataRequired()])
    city = StringField('Введите название города', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
'''
Форма входа пользователя

Расширение Flask-WTF использует классы Python для представления веб-форм.
Класс формы просто определяет поля формы как переменные класса.


Еще раз имея в виду разделение проблем, я собираюсь использовать новый app/forms.py модуль для хранения классов веб-форм.
Для начала определим форму входа пользователя, в которой пользователю будет предложено ввести имя пользователя и пароль.
Форма также будет включать флажок "Запомнить меня" и кнопку Отправить:
'''