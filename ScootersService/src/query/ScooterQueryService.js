import QUERY from "./scooters.query.js";
import db from "../config/mysql.config.js";
import log from "../config/logger.js";

export function getScooter(id, callback) {
    log.info(`Query for scooter ${id}`)
    db.query(QUERY.SELECT_SCOOTER_BY_ID, [id], (error, results) => {
        if (error) {
            callback(error, null);
            return;
        }
        callback(null, results);
    });
}
