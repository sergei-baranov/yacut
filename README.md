# yacut

Учебный проект - Сервис коротких ссылок.

Можно создавать и использовать короткие ссылки как в web-UI,
так и посредством REST HTTP API.

Реализация проекта: [Сергей Баранов](https://github.com/sergei-baranov/).

Проект реализован на `Flask`, использует `SQLAlchemy`, `Flask-Migrate`, `Flask-WTF`,
`Flask-SQLAlchemy`, соответствует спецификации `OpenAPI`.

## Установка

Создать виртуальное окружение и установить зависимости:

```bash
(venv) .../yacut$ pip install -r requirements.txt
```

Создать и наполнить файл `.env`, например учебно можно так:

```
FLASK_APP=yacut
FLASK_DEBUG=1
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=BOO_MOO_WOO
```

## Запуск

например изначально

```bash
(venv) .../yacut$ flask db init
(venv) .../yacut$ flask db migrate
(venv) .../yacut$ flask db upgrade
(venv) .../yacut$ flask --app yacut run --debug
```

далее просто

```bash
(venv) .../yacut$ flask --app yacut run
```

или

```bash
(venv) .../yacut$ flask run
```

## Использование

Ходить в веб-UI по адресу http://127.0.0.1:5000/ (или какой хост вы настроили)

Ходить в REST API на ендпойнты (see openapi.yaml)
