import express from "express";
import {getScooter, getScooters, createScooter, updateScooter, deleteScooter} from "../controller/scooters.controller.js";

const scooterRoutes = express.Router();

scooterRoutes.route('/')
    .get(getScooters)
    .post(createScooter);

scooterRoutes.route('/:id')
    .get(getScooter)
    .patch(updateScooter)
    .delete(deleteScooter)

export default scooterRoutes;