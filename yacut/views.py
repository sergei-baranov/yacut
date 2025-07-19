from flask import flash, redirect, render_template, request

from . import app, db
from .forms import URLMapForm
from .models import get_unique_short_id, URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        original = form.original_link.data
        if request.host in original:
            flash('Нельзя шортить ссылки на наш же хост.', 'original')
            return render_template('add_short_link.html', form=form)
        short = form.custom_id.data
        if short is None or short == '':
            short = get_unique_short_id()
        if URLMap.query.filter_by(short=short).first() is not None:
            flash(
                'Предложенный вариант короткой ссылки уже существует.',
                'short'
            )
            return render_template('add_short_link.html', form=form)
        urlmap = URLMap(
            original=original,
            short=short,
        )
        db.session.add(urlmap)
        db.session.commit()
        return render_template('add_short_link.html', form=form, urlmap=urlmap)
    return render_template('add_short_link.html', form=form)


@app.route('/<string:short>', methods=['GET', ])
def redirect_short_to_original(short: str):
    urlmap = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(urlmap.original, 302)
