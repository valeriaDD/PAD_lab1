import database from "../config/mysql.config.js";
import QUERY from "../query/scooters.query.js";
import log from "../config/logger.js";

export const getScootersIds = (_, callback) => {
    // database.query(QUERY.SELECT_SCOOTER_IDS, [], (error, result) => {
    //     if (error) {
    //         log.error(error.message);
    //          throw error
    //     } else {
    //         callback(null, result)
    //     }
    // })

    callback(null, 'testtt')
}