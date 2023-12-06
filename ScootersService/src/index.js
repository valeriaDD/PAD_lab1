import dotenv from "dotenv";
import grpcServer from "./proto/ScooterServer.js";
import {Client} from "@elastic/elasticsearch";

dotenv.config();
grpcServer;

const client = new Client({node: 'http://elasticsearch:9200'});

await client.index({
    body: { message: 'Scooter server started!' },
    index: 'scooter'
});
