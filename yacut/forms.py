import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 256), URL()]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(1, 16),
            Regexp(
                r'^[a-zA-Z0-9]{1,16}$',
                re.IGNORECASE,
                message='Введите 1...16 латинских букв и/или цифр'
            ),
        ]
    )
    submit = SubmitField('Создать')
