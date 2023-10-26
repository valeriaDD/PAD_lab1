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

// ServiceDiscoveryClient.DiscoverService({service_name: "bookings"}, {deadline: deadline}, (error, serviceInfo) => {
//     if (!error) {
//         BookingsClient(serviceInfo.host, serviceInfo.port)
//             .BookScooter({scooter_id: 1, start: '2023-12-25 23:50:55', user_email: "test", title: "test"}, (error, callback) => {
//                 if (error) log.error(error)
//                 if (callback) log.info(callback)
//             });
//     } else {
//         log.error('Failed to discover the service:', error);
//     }
// })


// ServiceDiscoveryClient.DiscoverService({service_name: "bookings"}, {deadline: deadline}, (error, serviceInfo) => {
//     if (!error) {
//         BookingsClient(serviceInfo.host, serviceInfo.port)
//             .endRide({id: 1}, (error, callback) => {
//                 if (error) log.error(error)
//                 if (callback) log.info(callback)
//             });
//
//     } else {
//         log.error('Failed to discover the service:', error);
//     }
// })