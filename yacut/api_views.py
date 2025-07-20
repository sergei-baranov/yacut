from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import get_unique_short_id, URLMap, validate_short_id_syntax


@app.route('/api/id/<string:short_id>/', methods=['GET'])
@app.route('/api/id/<string:short_id>', methods=['GET'])
def get_original(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': urlmap.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_urlmap():
    data = request.get_json(silent=True)

    if data is None:
        raise InvalidAPIUsage(
            'Отсутствует тело запроса', HTTPStatus.BAD_REQUEST)
    if 'url' not in data:
        raise InvalidAPIUsage(
            '"url" является обязательным полем!', HTTPStatus.BAD_REQUEST)
    if (
            'custom_id' in data
            and data['custom_id'] != ''
            and not validate_short_id_syntax(data['custom_id'])
    ):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки',
            HTTPStatus.BAD_REQUEST
        )
    if (
            'custom_id' in data
            and data['custom_id'] != ''
            and URLMap.query.filter_by(short=data['custom_id'])
            .first() is not None
    ):
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.',
            HTTPStatus.BAD_REQUEST
        )

    if 'custom_id' not in data or data['custom_id'] == '':
        data['custom_id'] = get_unique_short_id()

    urlmap = URLMap()
    urlmap.from_api_dict(data)
    db.session.add(urlmap)
    db.session.commit()

    return jsonify(urlmap.to_api_dict()), 201
