import * as protoLoader from "@grpc/proto-loader";
import * as grpc from "@grpc/grpc-js";

function createBookingClient(serverHost, serverPort) {
    let packageDefinition = protoLoader.loadSync(
        "./src/proto/files/bookings.proto",
        {
            keepCase: true,
            longs: String,
            enums: String,
            defaults: true,
            oneofs: true,
        }
    );
    const ScootersService = grpc.loadPackageDefinition(packageDefinition).BookingsService;

    return  new ScootersService(
        `${serverHost}:${serverPort}`,
        grpc.credentials.createInsecure()
    );
}

export default createBookingClient;

