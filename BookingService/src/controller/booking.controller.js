import BookingQueries from "../query/BookingsQuery.js";
import * as grpc from "@grpc/grpc-js";
import log from "../config/logger.js";


const queries = new BookingQueries();

export function bookScooter(call, callback) {
    log.info("Call for booking");
    const scooterId = call.request.scooter_id;

    queries.bookScooter(call.request, (err, result) => {
        if (err) {
            callback({
                code: grpc.status.INTERNAL,
                details: "Error while inserting into database"
            });
            return;
        }
        callback(null, result);
    });
}

export function endRide(call, callback) {
    queries.getBooking(call.request.id, (err, result) => {
        if (err) {
            callback({
                code: grpc.status.INTERNAL,
                details: "Error while retrieving from database"
            });
        } else if (!result) {
            callback({
                code: grpc.status.NOT_FOUND,
                details: "Booking not found"
            });
        } else {
            queries.endRide(call.request.id, (err, result) => {
                if (err) {
                    callback({
                        code: grpc.status.INTERNAL,
                        details: "Error while updating database"
                    });
                } else {
                    getBooking({request: {id: call.request.id}}, callback);
                }
            });
        }
    });
}

export function getBooking(call, callback) {
    log.info(`Query for book`)
    queries.getBooking(call.request.id, (err, result) => {
        if (err) {
            callback({
                code: grpc.status.INTERNAL,
                details: "Error while retrieving from database"
            });
        } else if (!result) {
            callback({
                code: grpc.status.NOT_FOUND,
                details: "Booking not found"
            });
        } else {
            callback(null, result);
        }
    });
}

export function getAllBookings(call, callback) {
    queries.getAllBookings((err, result) => {
        if (err) {
            callback({
                code: grpc.status.INTERNAL,
                details: "Error while retrieving from database"
            });
        } else {
            callback(null, {bookings: result});
        }
    });
}