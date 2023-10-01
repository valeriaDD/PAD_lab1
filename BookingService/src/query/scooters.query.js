const QUERY = {
    SELECT_SCOOTERS: `SELECT *
                      FROM scooters
                      ORDER BY created_at DESC`,

    SELECT_SCOOTER: `SELECT *
                     FROM scooters
                     WHERE id = ?`,


    DELETE_SCOOTER: `DELETE
                     FROM scooters
                     WHERE id = ?`,

    INSERT_SCOOTER: function (data) {
        let query = '';

        if (Object.keys(data).length !== 0) {
            const columns = Object.keys(data).join(', ');
            const values = Object.values(data)
                .map(value => typeof value === 'string' ? `'${value}'` : value)
                .join(', ');

            query = `INSERT INTO scooters (${columns})
                     VALUES (${values});`;
        }

        return query;
    },

    PATCH_SCOOTER: function (data, id) {
        let query = '';

        if (Object.keys(data).length !== 0) {
            query = `UPDATE scooters
                     SET `;
            query += Object.keys(data)
                .map((key) => `${key}=${typeof data[key] === 'string' ? `'${data[key]}'` : data[key]}`)
                .join(', ');

            query += ` WHERE id=${id};`;
        }

        return query;
    }
};


export default QUERY;