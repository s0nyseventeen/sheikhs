from sqlite3 import connect
from sqlite3 import PARSE_DECLTYPES
from sqlite3 import Row

from flask import current_app
from flask import g
from click import command
from click import echo


def get_db():
    if 'db' not in g:
        g.db = connect(
            current_app.config['DATABASE'],
            detect_types=PARSE_DECLTYPES
        )
        g.db.row_factory = Row
    return g.db


def __close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@command('init-db')
def __init_db_command():
    init_db()
    echo('Initialized the db')


def init_app(app):
    app.teardown_appcontext(__close_db)
    app.cli.add_command(__init_db_command)
