CREATE DATABASE IF NOT EXISTS scootersdb;

USE scootersdb;

DROP TABLE IF EXISTS scooters;
CREATE TABLE scooters
(
    id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    label       VARCHAR(64)     NOT NULL UNIQUE,
    battery     INT UNSIGNED    NOT NULL,
    location    VARCHAR(64)     NOT NULL,
    is_charging BOOLEAN         NOT NULL DEFAULT FALSE,
    available   BOOLEAN         NOT NULL DEFAULT FALSE,
    created_at  TIMESTAMP                DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP                DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)