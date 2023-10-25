import * as queries from "../query/ScooterQueryService.js";
import * as grpc from "@grpc/grpc-js";

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

        const scooter = result[0]; // Assuming result is an array and we're interested in the first entry
        callback(null, {
            id: scooter.id,
            label: scooter.label,
            battery: scooter.battery,
            location: scooter.location,
            is_charging: scooter.is_charging
        });
    });
}