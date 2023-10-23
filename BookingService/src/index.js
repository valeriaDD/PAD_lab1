import dotenv from "dotenv";
import log from "./config/logger.js";
import ScooterClient from "./proto/clients/ScooterClient.js";
import protoServer from "./proto/BookingServer.js";
import ServiceDiscoveryClient from "./proto/clients/ServiceDiscoveryClient.js";

dotenv.config();
protoServer;


ServiceDiscoveryClient.DiscoverService({service_name: "scooters"}, (error, serviceInfo) => {
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



