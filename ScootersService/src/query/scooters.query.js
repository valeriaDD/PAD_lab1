const QUERY = {
    SELECT_SCOOTERS: `SELECT *
                      FROM scooters
                      ORDER BY created_at DESC`,

    SELECT_SCOOTER: `SELECT *
                     FROM scooters
                     WHERE id ?`,

    INSERT_SCOOTER: `INSERT INTO scooters(label, battery, location, is_charging)
                     VALUES (?, ?, ?, ?)`,

    UPDATE_SCOOTER: `UPDATE scooters
                     SET label       = ?,
                         battery     = ?,
                         location    = ?,
                         is_charging = ?
                     WHERE id = ?`,

    DELETE_SCOOTER: `DELETE
                     FROM scooters
                     WHERE id = ?`
};

export default QUERY;