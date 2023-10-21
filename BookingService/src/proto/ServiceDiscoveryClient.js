import * as grpc from "@grpc/grpc-js";
import * as protoLoader from "@grpc/proto-loader";
import log from "../config/logger.js";

const serviceDiscoveryPackageDefinition = protoLoader.loadSync(
"./src/proto/service_discovery.proto",
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
    }
);

const serviceDiscovery = grpc.loadPackageDefinition(serviceDiscoveryPackageDefinition).ServiceRegistry;

const serviceDiscoveryClient = new serviceDiscovery(
    "service-discovery:2000",
    grpc.credentials.createInsecure()
);

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

    return serviceDiscoveryClient.RegisterService(serviceInfo, (error, callback) => {
        if (error) log.error(error)
        if (callback) log.info(callback)
    });
};