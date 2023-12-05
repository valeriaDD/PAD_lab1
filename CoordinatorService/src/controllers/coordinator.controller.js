import log from "../config/logger.js";
import ServiceDiscoveryClient from "../proto/clients/ServiceDiscoveryClient.js";
import * as grpc from "@grpc/grpc-js";
import ScooterClient from "../proto/clients/ScooterClient.js";
import BookingsClient from "../proto/clients/BookingsClient.js";

const DEADLINE_SECONDS = 5;

function createDeadline() {
    const deadline = new Date();
    deadline.setSeconds(deadline.getSeconds() + DEADLINE_SECONDS);
    return deadline;
}

function discoverService(serviceName, callback) {
    ServiceDiscoveryClient.DiscoverService({ service_name: serviceName }, { deadline: createDeadline() }, callback);
}

function handleServiceFailError(error, callback) {
    if (error) {
        console.error(`Error during service discovery: ${error}`);
        callback({ code: grpc.status.INTERNAL, details: "Error during service discovery" });
        return true;
    }
    return false;
}

function setScooterAvailability(scooterClient, scooterId, available, callback) {
    scooterClient.SetScooterAvailability({ id: scooterId, available }, callback);
}

export function book(call, callback) {
    log.info("Call for booking");
    const scooterId = call.request.scooter_id;

    discoverService("scooters", (error, serviceInfo) => {
        if (handleServiceFailError(error, callback)) return;

        const scooterClient = ScooterClient(serviceInfo.host, serviceInfo.port);
        setScooterAvailability(scooterClient, scooterId, false, (error) => {
            if (error) {
                log.error(`Error setting scooter availability: ${error}`);
                callback({ code: error.code, details: error.details });
                return;
            }

            discoverService("bookings", (error, serviceInfo) => {
                if (handleServiceFailError(error, callback)) {
                    setScooterAvailability(scooterClient, scooterId, true, handleServiceFailError);
                    return;
                }

                const bookingsClient = BookingsClient(serviceInfo.host, serviceInfo.port);
                bookingsClient.BookScooter(call.request, (error, response) => {
                    if (error) {
                        log.error(`Booking error: ${error}`);
                        setScooterAvailability(scooterClient, scooterId, true, handleServiceFailError);
                        callback({ code: error.code, details: error.details });
                        return;
                    }
                    callback(null, response);
                });
            });
        });
    });
}

export function endRide(call, callback) {
    log.info("Call for end ride");
    const bookingId = call.request.id;

    discoverService("bookings", (error, serviceInfo) => {
        if (handleServiceFailError(error, callback)) return;

        const bookingClient = BookingsClient(serviceInfo.host, serviceInfo.port);
        bookingClient.EndRide({ id: bookingId }, (error, response) => {
            if (error) {
                log.error(`Error ending ride: ${error}`);
                callback({ code: error.code, details: error.details });
                return;
            }

            discoverService("scooters", (error, serviceInfo) => {
                if (handleServiceFailError(error, callback)) return;

                const scooterClient = ScooterClient(serviceInfo.host, serviceInfo.port);
                setScooterAvailability(scooterClient, response.scooter_id, true, (error) => {
                    if (error) {
                        log.error(`Error setting scooter availability: ${error}`);
                    }
                });
                callback(null, response);
            });
        });
    });
}
