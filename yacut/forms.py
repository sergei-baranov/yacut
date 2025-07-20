from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (DataRequired, Length, Optional, URL,
                                ValidationError)

from .models import validate_short_id_syntax


def short_id_syntax_validator(form, field):
    if not validate_short_id_syntax(field.data):
        raise ValidationError('Введите 1...16 латинских букв и/или цифр')


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(max=256), URL()]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(max=16),
            short_id_syntax_validator,
        ]
    )
    submit = SubmitField('Создать')
