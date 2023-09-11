CREATE TABLE IF NOT EXISTS users (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	username VARCHAR(256) UNIQUE NOT NULL,
	email VARCHAR(256) UNIQUE NOT NULL,
	password VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS work (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	title VARCHAR(256) UNIQUE NOT NULL,
	created VARCHAR(256) NOT NULL,
	description VARCHAR(256),
	image VARCHAR(256)
);