CREATE DATABASE IF NOT EXISTS bookingsdb;

USE bookingsdb;

DROP TABLE IF EXISTS bookings;
CREATE TABLE bookings
(
    id             BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title          VARCHAR(64) NOT NULL,
    scooter_id     BIGINT UNSIGNED NOT NULL,
    user_email         VARCHAR(64)  NOT NULL,
    start          TIMESTAMP   NOT NULL,
    end            TIMESTAMP,
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

