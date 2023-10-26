import dotenv from "dotenv";
import log from "./config/logger.js";
import ScooterClient from "./proto/clients/ScooterClient.js";
import protoServer from "./proto/BookingServer.js";
import ServiceDiscoveryClient from "./proto/clients/ServiceDiscoveryClient.js";

dotenv.config();
protoServer;

// TODO: Add timeout to env value
const timeout = 5000; // 5 seconds
const deadline = new Date(Date.now() + timeout);

// ServiceDiscoveryClient.DiscoverService({service_name: "scooters"}, {deadline: deadline}, (error, serviceInfo) => {
//     if (!error) {
//         ScooterClient(serviceInfo.host, serviceInfo.port)
//             .GetScooter({id: 1}, (error, callback) => {
//                 if (error) log.error(error)
//                 if (callback) log.info(callback)
//             });
//     } else {
//         log.error('Failed to discover the service:', error);
//     }
// })

// ServiceDiscoveryClient.DiscoverService({service_name: "scooters"}, {deadline: deadline}, (error, serviceInfo) => {
//     if (!error) {
//         ScooterClient(serviceInfo.host, serviceInfo.port)
//             .createScooter({label: "test2", battery: 20, location: "Chisinau", is_charging: false}, (error, callback) => {
//                 if (error) log.error(error)
//                 if (callback) log.info(callback)
//             });
//     } else {
//         log.error('Failed to discover the service:', error);
//     }
// })


// ServiceDiscoveryClient.DiscoverService({service_name: "scooters"}, {deadline: deadline}, (error, serviceInfo) => {
//     if (!error) {
//         ScooterClient(serviceInfo.host, serviceInfo.port)
//             .deleteScooter({id: 8}, (error, callback) => {
//                 if (error) log.error(error)
//                 if (callback) log.info(callback)
//             });
//     } else {
//         log.error('Failed to discover the service:', error);
//     }
// })


