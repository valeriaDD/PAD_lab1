import * as queries from "../query/ScooterQueryService.js";
import * as grpc from "@grpc/grpc-js";
import log from "../config/logger.js";

export function getScooter(call, callback) {
    const scooterId = call.request.id;
    queries.getScooter(scooterId, (err, result) => {
        if (err) {
            callback({
                code: grpc.status.INTERNAL,
                details: "Error while fetching scooter from database"
            });
            return;
        }

        if (!result || result.length === 0) {
            callback({
                code: grpc.status.NOT_FOUND,
                details: "Scooter not found"
            });
            return;
        }

        const scooter = result[0];
        callback(null, {
            id: scooter.id,
            label: scooter.label,
            battery: scooter.battery,
            location: scooter.location,
            is_charging: scooter.is_charging
        });
    });
}

export function getAllScooters(_, callback) {
    queries.getAllScooters((err, results) => {
        if (err) {
            callback({
                code: grpc.status.INTERNAL,
                details: "Error while retrieving scooters from database"
            });
            return;
        }

        if (!results) {
            callback({
                code: grpc.status.NOT_FOUND,
                details: "No scooters found"
            });
            return;
        }

        const scooters = results.map(scooter => ({
            id: scooter.id,
            label: scooter.label,
            battery: scooter.battery,
            location: scooter.location,
            is_charging: scooter.is_charging
        }));
        callback(null, {scooters});
    });
}

export function updateScooter(call, callback) {
    const scooterData = {
        id: call.request.id,
        label: call.request.label,
        battery: call.request.battery,
        location: call.request.location,
        is_charging: call.request.is_charging
    };

    queries.updateScooter(scooterData, (err, result) => {
        if (err) {
            callback({
                code: grpc.status.INTERNAL,
                details: "Error while updating scooter in database"
            });
            return;
        }

        if (result.affectedRows === 0) {
            callback({
                code: grpc.status.NOT_FOUND,
                details: "Scooter not found"
            });
            return;
        }

        callback(null, {});
    });
}

export function deleteScooter(call, callback) {
    const scooterId = call.request.id;
    queries.deleteScooter(scooterId, (err, result) => {
        if (err) {
            callback({
                code: grpc.status.INTERNAL,
                details: "Error while deleting scooter from database"
            });
            return;
        }

        if (result.affectedRows === 0) {
            callback({
                code: grpc.status.NOT_FOUND,
                details: "Scooter not found"
            });
            return;
        }

        callback(null, {});
    });
}

export function createScooter(call, callback) {
    const data = {
        label: call.request.label,
        battery: call.request.battery,
        location: call.request.location,
        is_charging: call.request.is_charging
    };

    log.info(data)


    queries.createScooter(data, (err, result) => {
        if (err) {
            callback({
                code: grpc.status.INTERNAL,
                details: "Error while creating scooter in database"
            });
            return;
        }

        callback(null, {
            id: result.id,
            label: result.label,
            battery: result.battery,
            location: result.location,
            is_charging: result.is_charging
        });
    });
}
