import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import ip from "ip";
import log from "./config/logger.js";
import Http from "./utils/http.js";

dotenv.config();

const PORT = process.env.SERVER_PORT || 3000;
const app = express();

app.use(cors({origin: '*'}));
app.use(express.json());

app.get("/", (request, response) => {
        response.status(Http.OK.code).send('Scooters API');
    }
)

app.listen(PORT, () => log.info(`Server running on ${ip.address()}:${PORT}`))