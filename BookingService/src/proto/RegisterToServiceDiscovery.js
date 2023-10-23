import log from "../config/logger.js";
import ServiceDiscoveryClient from "./clients/ServiceDiscoveryClient.js";

export const registerWithServiceDiscovery = (
    serviceName,
    serviceHost,
    servicePort
) => {
    const serviceInfo = {
        service_name: serviceName,
        host: serviceHost,
        port: servicePort,
    };

    return ServiceDiscoveryClient.RegisterService(serviceInfo, (error, callback) => {
        if (error) log.error(error)
        if (callback) log.info(callback)
    });
};