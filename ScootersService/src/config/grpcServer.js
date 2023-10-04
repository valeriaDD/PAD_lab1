import ip from "ip";
import * as protoLoader from "@grpc/proto-loader";
import * as grpc from "@grpc/grpc-js";
import log from "./logger.js";

const GRPC_PORT = process.env.GRPC_SERVER_PORT || 30001;
const GRPC_SERVER_HOST = process.env.GRPC_SERVER_HOST|| ip.address();
const GRPC_SERVER_PORT = `${GRPC_SERVER_HOST}:${GRPC_PORT}`

let scooterPackageDefinition = protoLoader.loadSync(
    "./src/proto/scooters.proto",
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
    }
);
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


const protoServer = new grpc.Server();

const scooterServiceProto = grpc.loadPackageDefinition(scooterPackageDefinition);
protoServer.addService(scooterServiceProto.ScootersService.service, {
    getScootersIds: (_, callback) => {
        log.info("GRPC call to getScootersIds")
        callback(null, {"scooter": [{id: 1}]});
    },
});

const bookingServiceProto = grpc.loadPackageDefinition(bookingPackageDefinition);
protoServer.addService(bookingServiceProto.BookingsService.service, {
    getBookingsIds: (_, callback) => {
        log.info("GRPC call to getBookingsIds")
        callback(null, {"booking": [{id: 1}]});
    },
});

protoServer.bindAsync(
    GRPC_SERVER_PORT,
    grpc.ServerCredentials.createInsecure(),
    (error, port) => {
        log.info(`Proto server running at ${GRPC_SERVER_PORT}`);
        protoServer.start();
    }
);


export default protoServer;