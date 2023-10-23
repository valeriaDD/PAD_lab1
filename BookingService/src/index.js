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

ServiceDiscoveryClient.DiscoverService({service_name: "scooters"}, {deadline: deadline}, (error, serviceInfo) => {
    if (!error) {
        ScooterClient(serviceInfo.host, serviceInfo.port)
            .getScootersIds({}, (error, callback) => {
                if (error) log.error(error)
                if (callback) log.info(callback)
            });
    } else {
        console.error('Failed to discover the service:', error);
    }
})



