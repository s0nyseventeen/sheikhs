DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS image;
DROP TABLE IF EXISTS work CASCADE;

CREATE TABLE users (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	username VARCHAR(256) UNIQUE NOT NULL,
	email VARCHAR(256) UNIQUE NOT NULL,
	password VARCHAR(256) NOT NULL
);

CREATE TABLE work (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	title VARCHAR(256) UNIQUE NOT NULL,
	created VARCHAR(256) NOT NULL,
	description TEXT
);

CREATE TABLE image (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	title VARCHAR(256) UNIQUE NOT NULL,
	description TEXT,
	work_id BIGINT REFERENCES work(id)
);
