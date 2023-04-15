CREATE TABLE IF NOT EXISTS users (
    slug varchar(50) not null,
    username varchar(50) not null,
    password varchar(50) not null,
    PRIMARY KEY (slug)
);