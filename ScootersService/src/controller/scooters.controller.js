import log from "../config/logger.js";
import database from "../config/mysql.config.js";
import QUERY from "../query/scooters.query.js";
import Http from "../utils/http.js";

export const getScooters = (req, res) => {
    log.info(`${req.method} ${req.originalUrl}, get all scooters.`);

    database.query(QUERY.SELECT_SCOOTERS, [], (error, result) => {
        if (error) {
            log.error(error.message)
            res.status(Http.INTERNAL_SERVER_ERROR.code).send(Http.INTERNAL_SERVER_ERROR.status);
        } else {
            res.status(Http.OK.code).send(result ? {data: result} : {});
        }
    });
}

export const createScooter = (req, res) => {
    log.info(`${req.method} ${req.originalUrl}, create scooter.`);

    database.query(QUERY.INSERT_SCOOTER(req.body), [], (error, result) => {
        if (error) {
            log.error(error.message);
            res.status(Http.INTERNAL_SERVER_ERROR.code).send(error);
        } else {
            res.status(Http.CREATED.code).send();
        }
    })
}

export const getScooter = (req, res) => {
    log.info(`${req.method} ${req.originalUrl}, get scooter.`);

    database.query(QUERY.SELECT_SCOOTER, [req.params.id], (error, result) => {
        if (result && result[0]) {
            res.status(Http.OK.code).send({data: result});
        } else {
            log.error(`Patient with ${req.params.id} not found`);
            res.status(Http.NOT_FOUND.code).send(Http.NOT_FOUND.status);
        }
    });
}

export const updateScooter = (req, res) => {
    log.info(`${req.method} ${req.originalUrl}, fetch scooter.`);

    database.query(QUERY.SELECT_SCOOTER, [req.params.id], (error, result) => {
        if (result[0]) {
            log.info(`${req.method} ${req.originalUrl}, update scooter.`);

            database.query(QUERY.PATCH_SCOOTER(req.body, req.params.id), [], (error, result) => {
                if (error) {
                    log.error(error.message);
                    res.status(Http.INTERNAL_SERVER_ERROR.code).send(error);
                } else {
                    res.status(Http.NO_CONTENT.code).send(Http.NO_CONTENT.status);
                }
            });

        } else {
            log.error(`Patient with ${req.params.id} not found`);
            res.status(Http.NOT_FOUND.code).send(Http.NOT_FOUND.status);
        }
    });
}


export const deleteScooter = (req, res) => {
    log.info(`${req.method} ${req.originalUrl}, deleting scooter.`);

    database.query(QUERY.DELETE_SCOOTER, [req.params.id], (error, result) => {
        if (result.affectedRows > 0) {
            res.status(Http.NO_CONTENT.code).send(Http.NO_CONTENT.status);
        } else {
            res.status(Http.NOT_FOUND.code).send(Http.NOT_FOUND.status);
        }
    });
}