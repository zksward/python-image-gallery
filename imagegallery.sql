CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    full_name VARCHAR NOT NULL,
    is_admin BOOLEAN DEFAULT 'f'
);

CREATE TABLE IF NOT EXISTS images (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) NOT NULL,
    s3_key VARCHAR NOT NULL
);

INSERT INTO users(username, password, full_name, is_admin) VALUES ('dongji', 'cpsc4973', 'Dongji Feng', 't');
INSERT INTO users(username, password, full_name, is_admin) VALUES ('sward', 'smw0036', 'Stephen Ward', 't');