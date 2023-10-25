import BookingQueries from "../query/BookingsQuery.js";
import * as grpc from "@grpc/grpc-js";
import ServiceDiscoveryClient from "../proto/clients/ServiceDiscoveryClient.js";
import ScooterClient from "../proto/clients/ScooterClient.js";
import log from "../config/logger.js";


const queries = new BookingQueries();

export function bookScooter(call, callback) {
    log.info("Call for booking");
    const scooterId = call.request.scooter_id;
    const deadline = new Date();
    deadline.setSeconds(deadline.getSeconds() + 5); // For example, setting a deadline of 5 seconds

    ServiceDiscoveryClient.DiscoverService({service_name: "scooters"}, {deadline: deadline}, (error, serviceInfo) => {
        if (error) {
            callback({
                code: grpc.status.INTERNAL,
                details: "Error during service discovery"
            });
            return;
        }

        const scooterClient = ScooterClient(serviceInfo.host, serviceInfo.port);
        scooterClient.getScooter({id: scooterId}, (error, scooterInfo) => {
            if (error) {
                log.info(`Scooter ${scooterId} not found!`);
                callback({
                    code: grpc.status.NOT_FOUND,
                    details: "Scooter ID not found"
                });
                return;
            }

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
        });
    });
}

export function endRide(call, callback) {
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

export function getBooking(call, callback) {
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