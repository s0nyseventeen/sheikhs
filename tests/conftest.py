import os
from pathlib import Path

from pytest import fixture

from basic import create_app
from basic.db import get_db

INSERT_INTO_WORK = """
    INSERT INTO work (title, created, description, image) VALUES
        ('Test title', '2023-06-05 00:00:00', 'New design', 'someimage.jpg');
"""
DEFAULT_USER = {'username': 'test', 'password': 'test', 'email': 'test@mail.ua'}


@fixture
def app():
    app = create_app({'TESTING': True})
    with (
        open(Path().resolve() / 'tests/queries.sql') as f,
        app.app_context()
    ):
        db = get_db()
        db.run_query(f.read())

    yield app

    with app.app_context():
        db = get_db()
        for query in 'DROP TABLE users;', 'DROP TABLE work;':
            db.run_query(query)

    __remove_image(app)


def __remove_image(app):
    for image in 'someimage.jpg', 'updated.jpg':
        try:
            path = Path(app.config['UPLOAD_FOLDER'])
            os.remove(path / image)
        except FileNotFoundError:
            pass


@fixture
def client(app):
    return app.test_client()


class AuthActions:
    def __init__(self, client):
        self.__client = client

    def login(self, username='test', password='test'):
        return self.__client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self.__client.get('/auth/logout')

    def register(self, data):
        return self.__client.post('/auth/register', data=data)


@fixture
def auth(client):
    return AuthActions(client)