CREATE table if not exists servers (
    id SERIAL PRIMARY KEY,
    server VARCHAR(100),
    cost INTEGER
);