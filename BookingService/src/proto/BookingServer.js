import ip from "ip";
import * as protoLoader from "@grpc/proto-loader";
import * as grpc from "@grpc/grpc-js";
import log from "../config/logger.js";
import {registerWithServiceDiscovery} from "./RegisterToServiceDiscovery.js";

const GRPC_PORT = process.env.SERVER_PORT || 3000;
const GRPC_SERVER_HOST = process.env.SERVICE_NAME || ip.address();
const GRPC_SERVER_PORT = `${GRPC_SERVER_HOST}:${GRPC_PORT}`;

let bookingPackageDefinition = protoLoader.loadSync(
    "./src/proto/bookings.proto",
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
    }
);

let serviceRegistryPackageDefinition = protoLoader.loadSync(
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

const bookingServiceProto = grpc.loadPackageDefinition(bookingPackageDefinition);
const serviceRegistryProto = grpc.loadPackageDefinition(serviceRegistryPackageDefinition);
protoServer.addService(bookingServiceProto.BookingsService.service, {
    getBookingsIds: (_, callback) => {
        log.info("GRPC call to getBookingsIds")
        callback(null, {"booking": [{id: 1}]});
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
        registerWithServiceDiscovery('bookings', GRPC_SERVER_HOST, GRPC_PORT)

        protoServer.start();
    }
);

export default protoServer;