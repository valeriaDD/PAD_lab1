import dotenv from "dotenv";
import protoServer from "./proto/BookingServer.js";
import {Client} from "@elastic/elasticsearch";
dotenv.config();
protoServer;

const client = new Client({node: 'http://elasticsearch:9200'});

await client.index({
    body: { message: 'Booking server started!' },
    index: 'booking'
});

