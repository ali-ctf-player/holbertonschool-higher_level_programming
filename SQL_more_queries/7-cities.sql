-- Cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- USE
USE htbn_0d_usa;

-- create
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id),
    Foreign Key (state_id) REFERENCES states(id)
);
