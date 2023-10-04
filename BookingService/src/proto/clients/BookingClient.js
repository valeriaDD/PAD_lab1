import * as protoLoader from "@grpc/proto-loader";
import * as grpc from "@grpc/grpc-js";
import ip from "ip";

const GRPC_SERVER_PORT = process.env.GRPC_SERVER_PORT || 30001;
const GRPC_SERVER_HOST = process.env.GRPC_SERVER_HOST|| ip.address();

let packageDefinition = protoLoader.loadSync(
    "./src/proto/bookings.proto",
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
    }
);
const BookingsService = grpc.loadPackageDefinition(packageDefinition).BookingsService;

const BookingsClient = new BookingsService(
    `${GRPC_SERVER_HOST}:${GRPC_SERVER_PORT}`,
    grpc.credentials.createInsecure()
);

export default BookingsClient;
