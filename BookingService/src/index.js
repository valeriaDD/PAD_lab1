import dotenv from "dotenv";
import log from "./config/logger.js";
import ScooterClient from "./proto/ScooterClient.js";
import protoServer from "./proto/BookingServer.js";

dotenv.config();
protoServer;

ScooterClient(process.env.GRPC_SERVER_HOST, process.env.GRPC_SERVER_PORT)
    .getScootersIds({}, (error, callback) => {
        if (error) log.error(error)
        if (callback) log.info(callback)
    });

