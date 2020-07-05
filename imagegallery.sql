CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    full_name VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS images (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) NOT NULL,
    s3_key VARCHAR NOT NULL
);

INSERT INTO users(username, password, full_name) VALUES ('dongji', 'cpsc4973', 'Dongji Feng');