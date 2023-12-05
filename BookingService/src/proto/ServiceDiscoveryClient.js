import * as protoLoader from "@grpc/proto-loader";
import * as grpc from "@grpc/grpc-js";

const serverHost = 'service-discovery'
const serverPort = '2000'

const packageDefinition = protoLoader.loadSync(
    "./src/proto/files/service_discovery.proto",
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
    }
);
const ServiceDiscoveryClient = grpc.loadPackageDefinition(packageDefinition).ServiceRegistry;

export default new ServiceDiscoveryClient(
    `${serverHost}:${serverPort}`,
    grpc.credentials.createInsecure()
);

