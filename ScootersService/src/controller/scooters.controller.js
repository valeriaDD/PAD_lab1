import log from "../config/logger.js";
import database from "../config/mysql.config.js";
import QUERY from "../query/scooters.query.js";
import Http from "../utils/http.js";

export const getScooters = (req, res) => {
    log.info(`${req.method} ${req.originalUrl}, get all scooters.`);

    database.query(QUERY.SELECT_SCOOTERS, (error, result) => {
        res.status(Http.OK.code).send(result ? {data: result} : {});
    });
}

export const createScooter = (req, res) => {
    log.info(`${req.method} ${req.originalUrl}, create scooter.`);

    database.query(QUERY.INSERT_SCOOTER, Object.values(req.body), (error, result) => {
        if (!result) {
            log.error(error.message);
            res.status(Http.INTERNAL_SERVER_ERROR.code);
        } else {
            res.status(Http.CREATED.code).send({data: result});
        }
    })
}