import db from "../config/mysql.config.js";
import log from "../config/logger.js";

class BookingQueries {
    bookScooter(data, callback) {
        const query = `
            INSERT INTO bookings (scooter_id, start, user_email, title)
            VALUES ('${data.scooter_id}', '${data.start}', '${data.user_email}', '${data.title}');
        `;
        db.query(query, (err, results) => {
            if (err) {
                log.error(err)
                return callback(err, null);
            }
            return callback(null, { id: results.insertId, ...data, end: "" });
        });
    }

    endRide(id, callback) {
        const query = `UPDATE bookings SET end = CURRENT_TIMESTAMP WHERE id = ${id}`;
        db.query(query, (err, results) => {
            if (err) {
                return callback(err, null);
            }
            return callback(null, results);
        });
    }

    getBooking(id, callback) {
        const query = `SELECT * FROM bookings WHERE id = ${id}`;
        db.query(query, (err, results) => {
            if (err) {
                return callback(err, null);
            }
            return callback(null, results[0]);
        });
    }

    getAllBookings(callback) {
        const query = 'SELECT * FROM bookings';
        db.query(query, (err, results) => {
            if (err) {
                log.error(err)
                return callback(err, null);
            }
            return callback(null, results);
        });
    }
}

export default BookingQueries;
