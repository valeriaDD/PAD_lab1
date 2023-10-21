import * as protoLoader from "@grpc/proto-loader";
import * as grpc from "@grpc/grpc-js";

function createScooterClient(serverHost, serverPort) {
    let packageDefinition = protoLoader.loadSync(
        "./src/proto/scooters.proto",
        {
            keepCase: true,
            longs: String,
            enums: String,
            defaults: true,
            oneofs: true,
        }
    );
    const ScootersService = grpc.loadPackageDefinition(packageDefinition).ScootersService;

    return  new ScootersService(
        `${serverHost}:${serverPort}`,
        grpc.credentials.createInsecure()
    );
}

export default createScooterClient;

