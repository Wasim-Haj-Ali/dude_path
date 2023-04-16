CREATE TABLE IF NOT EXISTS indicators (
    slug varchar(50) not null,
    name varchar(50) not null,
    userslug varchar(50) not null,
    content varchar(255),
    PRIMARY KEY (slug),
    FOREIGN KEY (userslug) REFERENCES users(slug)
);