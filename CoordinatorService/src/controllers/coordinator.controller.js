import log from "../config/logger.js";

export function book(call, callback) {
    log.info("Call for book")
    callback(null, {
        id: 1,
        start: '25 dec 18:00',
        user_email: 'test@email.com',
        scooter_id: '4',
        end: "",
        title: 'test',
    })
}

export function endRide(call, callback) {
    log.info("Call for end ride")
    callback(null, {
        id: 1,
        start: '25 dec 18:00',
        user_email: 'test@email.com',
        scooter_id: '4',
        end: "25 dec 19:00",
        title: 'test',
    })
}