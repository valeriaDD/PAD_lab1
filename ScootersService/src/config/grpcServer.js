import ip from "ip";
import * as protoLoader from "@grpc/proto-loader";
import * as grpc from "@grpc/grpc-js";
import log from "./logger.js";

const GRPC_PORT = process.env.GRPC_SERVER_PORT || 30001;
const GRPC_SERVER_HOST = process.env.GRPC_SERVER_HOST|| ip.address();
const PROTO_PATH = "./src/proto/scooters.proto";
const GRPC_SERVER_PORT = `${GRPC_SERVER_HOST}:${GRPC_PORT}`

let packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
    }
);
const bookingsProto = grpc.loadPackageDefinition(packageDefinition);
const protoServer = new grpc.Server();

protoServer.addService(bookingsProto.ScootersService.service, {
    getScootersIds: (_, callback) => {
        log.info("GRPC call to getScootersIds")
        callback(null, 'test');
    },
});

protoServer.bindAsync(
    GRPC_SERVER_PORT,
    grpc.ServerCredentials.createInsecure(),
    (error, port) => {
        log.info(`Proto server running at ${GRPC_SERVER_PORT}:${GRPC_PORT}`);
        protoServer.start();
    }
);


export default protoServer;