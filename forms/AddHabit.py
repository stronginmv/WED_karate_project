from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, IntegerField

from wtforms.validators import DataRequired


class AddHabitForm(FlaskForm):
    habit_name = StringField('Название достижения', validators=[DataRequired()])
    duration = IntegerField('Какое место заняли', validators=[DataRequired()])
    about_habit = StringField('Описание пути к вашей победе', validators=[DataRequired()])
    submit = SubmitField('Добавить')
