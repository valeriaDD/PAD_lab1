CREATE DATABASE IF NOT EXISTS bookingsdb;

USE bookingsdb;

DROP TABLE IF EXISTS users;
CREATE TABLE users
(
    id            BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email         VARCHAR(64)  NOT NULL UNIQUE,
    phone         VARCHAR(64)  NOT NULL UNIQUE,
    payment_token VARCHAR(256) NOT NULL,
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


DROP TABLE IF EXISTS bookings;
CREATE TABLE bookings
(
    id             BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title          VARCHAR(64) NOT NULL,
    scooter_id     BIGINT UNSIGNED NOT NULL,
    user_id        BIGINT UNSIGNED NOT NULL,
    start          TIMESTAMP   NOT NULL,
    end            TIMESTAMP,
    price          INT UNSIGNED NOT NULL DEFAULT 0,
    payment_status TINYINT UNSIGNED NOT NULL DEFAULT 0,
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

