import ServiceDiscoveryClient from "../clients/ServiceDiscoveryClient.js";
import log from "../../config/logger.js";

const timeout = 5000; // 5 seconds
const deadline = new Date(Date.now() + timeout);

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

    return ServiceDiscoveryClient.RegisterService(serviceInfo, {deadline: deadline} ,(error, callback) => {
        if (error) log.error(error)
        if (callback) log.info(callback)
    });
};