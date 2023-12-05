import log from "../config/logger.js";
import ServiceDiscoveryClient from "../proto/clients/ServiceDiscoveryClient.js";
import * as grpc from "@grpc/grpc-js";
import ScooterClient from "../proto/clients/ScooterClient.js";
import BookingsClient from "../proto/clients/BookingsClient.js";

export function book(call, callback) {
    log.info("Call for booking");
    const scooterId = call.request.scooter_id;
    const deadline = new Date();
    deadline.setSeconds(deadline.getSeconds() + 5);

    ServiceDiscoveryClient.DiscoverService({service_name: "scooters"}, {deadline: deadline}, (error, serviceInfo) => {
        console.log(`Call to discover scooter service`);
        if (error) {
            callback({code: grpc.status.INTERNAL, details: "Error during service discovery"});
            return;
        }

        const scooterClient = ScooterClient(serviceInfo.host, serviceInfo.port);
        scooterClient.SetScooterAvailability({id: scooterId, available: false}, (error, scooterInfo) => {
            console.log(`Call to mark scooter unavailable`);
            if (error) {
                callback({code: error.code, details: error.details});
                return;
            }

            ServiceDiscoveryClient.DiscoverService({service_name: "bookings"}, {deadline: deadline}, (error, serviceInfo) => {
                if (error) {
                    log.info(`Error during service discovery`);
                    scooterClient.SetScooterAvailability({id: scooterId, available: true}, (error, scooterInfo) => {
                        console.log(`Rollback scooter service`);
                        if (error) {
                            callback({code: error.code, details: error.details});
                        }
                    });

                    callback({code: error.code, details: error.details});
                    return;
                }

                const bookingsClient = BookingsClient(serviceInfo.host, serviceInfo.port);
                bookingsClient.BookScooter(call.request, (error, response) => {
                    if (error) {
                        log.info(`Booking error!`);
                        scooterClient.SetScooterAvailability({id: scooterId, available: true}, (error, scooterInfo) => {
                            console.log(`Rollback scooter service`);
                            if (error) {
                                callback({code: error.code, details: error.details});
                            }
                        });
                        callback({code: error.code, details: error.details});
                        return;
                    }

                    callback(null, response)
                });
            });
        });
    });
}

export function endRide(call, callback) {
    log.info("Call for end ride");
    const bookingId = call.request.id;
    const deadline = new Date();
    deadline.setSeconds(deadline.getSeconds() + 5);

    ServiceDiscoveryClient.DiscoverService({service_name: "bookings"}, {deadline: deadline}, (error, serviceInfo) => {
        console.log(`Call to discover bookings service`);
        if (error) {
            console.error(`Error for bookings service discovery`);
            callback({code: grpc.status.INTERNAL, details: "Error during service discovery"});
            return;
        }

        const bookingClient = BookingsClient(serviceInfo.host, serviceInfo.port);
        bookingClient.EndRide({id: bookingId}, (error, response) => {
            console.log(`Call to end ride ${bookingId}`);
            if (error) {
                console.log(`Error for call to end ride ${bookingId}`);
                callback({code: error.code, details: error.details});
                return;
            }

            const scooterId = response.scooter_id;

            ServiceDiscoveryClient.DiscoverService({service_name: "scooters"}, {deadline: deadline}, (error, serviceInfo) => {
                console.log(`Call to discover scooters service`);
                if (error) {
                    console.error(`Error for scooters service discovery`);
                    callback({code: grpc.status.INTERNAL, details: "Error during service discovery"});
                    return;
                }

                const scooterClient = ScooterClient(serviceInfo.host, serviceInfo.port);
                scooterClient.SetScooterAvailability({id: scooterId, available: true}, (error, response) => {
                    console.log(`Call to mark scooter available ${scooterId}`);
                    if (error) {
                        console.log(`Unable to mark availability of scooter ${scooterId}`)
                    }
                });

                callback(null, response)
            });
        });
    });
}