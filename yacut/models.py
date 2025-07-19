from datetime import datetime
import random
import string

import flask

from . import db


def get_unique_short_id() -> str:
    shield = 100
    while True:
        shield -= 1
        short = ''.join(
            random.choices(string.ascii_letters + string.digits, k=6)
        )
        if URLMap.query.filter_by(short=short).first() is None:
            break
        if shield == 0:
            short = None
            break
    return short


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_api_dict(self):
        return dict(
            url=self.original,
            short_link=flask.request.host_url + self.short,
        )

    def from_api_dict(self, data):
        if 'url' in data:
            setattr(self, 'original', data['url'])
        if 'custom_id' in data:
            setattr(self, 'short', data['custom_id'])
