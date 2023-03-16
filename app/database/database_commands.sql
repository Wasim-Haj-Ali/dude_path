CREATE DATABASE indicator_database;

use indicator_database;


CREATE TABLE indicators (
    slug varchar not null,
    content varchar(255),
    PRIMARY KEY (slug)
);

INSERT INTO indicators(slug, content) VALUES ("abc123", "Hello abc123");