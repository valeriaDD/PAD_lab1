import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import ip from "ip";
import log from "./config/logger.js";
import ScooterClient from "./proto/ScooterClient.js";
import Http from "./utils/http.js";
import scooterRoutes from "./routes/scooters.routes.js";


dotenv.config();

const PORT = process.env.SERVER_PORT || 3000;
const TIMEOUT = 600;
const app = express();

app.use(cors({origin: '*'}));
app.use(express.json());
app.use('/scooters', scooterRoutes);

app.get("/", (req, res) => {
        ScooterClient.getScootersIds({}, {deadline: TIMEOUT }, (error, test) => {
            if (error) log.error(error)
            if (test) {
                log.info(test)
                res.status(Http.OK.code).send(test);
            } else {
                res.status(Http.OK.code).send("hi from booking");
            }
        });
    }
)

app.all("*", (req, res) => {
        res.status(Http.NOT_FOUND.code).send(Http.NOT_FOUND.status);
    }
)

app.listen(PORT, () => log.info(`Server running on ${ip.address()}:${PORT}`))