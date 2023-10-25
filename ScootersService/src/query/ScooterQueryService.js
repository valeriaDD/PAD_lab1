import db from "../config/mysql.config.js";

export function getScooter(id, callback) {
    const query = `SELECT * FROM scooters WHERE id = ?`;
    db.query(query, [id], (error, results) => {
        if (error) {
            callback(error, null);
        } else {
            callback(null, results);
        }
    });
}

export function getAllScooters(callback) {
    const query = `SELECT * FROM scooters`;
    db.query(query, [], (error, results) => {
        if (error) {
            callback(error, null);
        } else {
            callback(null, results);
        }
    });
}

export function updateScooter(data, callback) {
     let updateCols = [];
    let values = [];

    for (let key in data) {
        if (data[key] !== undefined && key !== 'id') {
            updateCols.push(`${key} = ?`);
            values.push(data[key]);
        }
    }

    if (updateCols.length === 0) {
        callback(new Error("No valid fields provided for update"), null);
        return;
    }

    let updateString = updateCols.join(', ');
    values.push(data.id);

    const query = `UPDATE scooters SET ${updateString} WHERE id = ?`;
    db.query(query, values, (error, results) => {
        if (error) {
            callback(error, null);
        } else {
            callback(null, results);
        }
    });
}

export function deleteScooter(id, callback) {
    const query = `DELETE FROM scooters WHERE id = ?`;
    db.query(query, [id], (error, results) => {
        if (error) {
            callback(error, null);
        } else {
            callback(null, results);
        }
    });
}

export function createScooter(data, callback) {
    const query = `INSERT INTO scooters (label, battery, location, is_charging) VALUES (?, ?, ?, ?)`;
    const values = [data.label, data.battery, data.location, data.is_charging];
    db.query(query, values, (error, results) => {
        if (error) {
            callback(error, null);
        } else {
            data.id = results.insertId;
            callback(null, data);
        }
    });
}
