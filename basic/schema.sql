DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS work;

CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	email TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL
);

CREATE TABLE work (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT UNIQUE NOT NULL,
	created TEXT NOT NULL,
	description TEXT,
	image TEXT
);
