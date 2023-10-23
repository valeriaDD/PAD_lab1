import ip from "ip";
import * as protoLoader from "@grpc/proto-loader";
import * as grpc from "@grpc/grpc-js";
import log from "../config/logger.js";
import {registerWithServiceDiscovery} from "./ServiceDiscoveryClient.js";

const GRPC_PORT = process.env.SERVER_PORT || 3000;
const GRPC_SERVER_HOST = process.env.SERVICE_NAME || ip.address();
const GRPC_SERVER_PORT = `${GRPC_SERVER_HOST}:${GRPC_PORT}`

const scooterPackageDefinition = protoLoader.loadSync(
    "./src/proto/scooters.proto",
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
    }
);

const serviceRegistryPackageDefinition = protoLoader.loadSync(
    "./src/proto/service_discovery.proto",
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
    }
);

const protoServer = new grpc.Server();

const scooterServiceProto = grpc.loadPackageDefinition(scooterPackageDefinition);
const serviceRegistryProto = grpc.loadPackageDefinition(serviceRegistryPackageDefinition);

protoServer.addService(scooterServiceProto.ScootersService.service,{
    getScootersIds: (_, callback) => {
        log.info("GRPC call to getScootersIds")
        callback(null, {"scooter": [{id: 1}]});
    },
});

protoServer.addService(serviceRegistryProto.ServiceRegistry.service, {
    CheckHealth: (_, callback) => {
        log.info("Health check!!")
        callback(null, {"status": true});
    }
});

protoServer.bindAsync(
    GRPC_SERVER_PORT,
    grpc.ServerCredentials.createInsecure(),
    (error, port) => {
        log.info(`Proto server running at ${GRPC_SERVER_PORT}`);
        registerWithServiceDiscovery('scooters', GRPC_SERVER_HOST, GRPC_PORT)

        protoServer.start();
    }
);


export default protoServer;