import * as protoLoader from "@grpc/proto-loader";
import * as grpc from "@grpc/grpc-js";
import ip from "ip";

const GRPC_SERVER_PORT = process.env.GRPC_SERVER_PORT || 30001;
const GRPC_SERVER_HOST = process.env.GRPC_SERVER_HOST|| ip.address();
const PROTO_PATH = "./src/proto/scooters.proto";

var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
    }
);
const ScootersService = grpc.loadPackageDefinition(packageDefinition).ScootersService;

const client = new ScootersService(
    `${GRPC_SERVER_HOST}:${GRPC_SERVER_PORT}`,
    grpc.credentials.createInsecure()
);

console.log(client)

export default client;
