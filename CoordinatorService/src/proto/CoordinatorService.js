import ip from "ip";
import * as protoLoader from "@grpc/proto-loader";
import * as grpc from "@grpc/grpc-js";
import log from "../config/logger.js";
import {registerWithServiceDiscovery} from "./services/RegisterToServiceDiscovery.js";
import {book, endRide} from "../controllers/coordinator.controller.js";

const GRPC_PORT = process.env.SERVER_PORT || 7000;
const GRPC_SERVER_HOST = process.env.SERVICE_NAME || ip.address();
const GRPC_SERVER_PORT = `${GRPC_SERVER_HOST}:${GRPC_PORT}`

const coordinatorPackageDefinition = protoLoader.loadSync(
    "./src/proto/files/coordinator.proto",
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
    }
);

const serviceRegistryPackageDefinition = protoLoader.loadSync(
    "./src/proto/files/service_discovery.proto",
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
    }
);

const protoServer = new grpc.Server();

const scooterServiceProto = grpc.loadPackageDefinition(coordinatorPackageDefinition);
const serviceRegistryProto = grpc.loadPackageDefinition(serviceRegistryPackageDefinition);

protoServer.addService(scooterServiceProto.Coordinator.service, {
    BookScooter: book,
    EndRide: endRide,
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
        registerWithServiceDiscovery('coordinator', GRPC_SERVER_HOST, GRPC_PORT)

        protoServer.start();
    }
);

export default protoServer;