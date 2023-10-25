import dotenv from "dotenv";
import grpcServer from "./proto/ScooterServer.js";
import ServiceDiscoveryClient from "./proto/clients/ServiceDiscoveryClient.js";
import log from "./config/logger.js";
import BookingsClient from "./proto/clients/BookingsClient.js";

dotenv.config();
grpcServer;

const timeout = process.env.TIMEOUT ?? 5000;
const deadline = new Date(Date.now() + timeout);

// ServiceDiscoveryClient.DiscoverService({service_name: "bookings"}, {deadline: deadline}, (error, serviceInfo) => {
//     if (!error) {
//         BookingsClient(serviceInfo.host, serviceInfo.port)
//             .GetAllBookings({}, (error, callback) => {
//                 if (error) log.error(error)
//                 if (callback) log.info(callback)
//             });
//     } else {
//         log.error('Failed to discover the service:', error);
//     }
// })

ServiceDiscoveryClient.DiscoverService({service_name: "bookings"}, {deadline: deadline}, (error, serviceInfo) => {
    if (!error) {
        BookingsClient(serviceInfo.host, serviceInfo.port)
            .BookScooter({scooter_id: 1, start:  new Date(), user_email: "test"}, (error, callback) => {
                if (error) log.error(error)
                if (callback) log.info(callback)
            });
    } else {
        log.error('Failed to discover the service:', error);
    }
})