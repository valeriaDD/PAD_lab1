from flask import Flask, request
from flask_caching import Cache

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)


@app.route("/")
@cache.cached(timeout=5)
def hello_world():
    return "hello"


@app.route('/book/scooters/<int:scooter_id>', methods=['POST'])
def book_scooter(scooter_id):
    data = request.json
    booking = {
        'id': 1,
        'title': data['title'],
        'start': data['start'],
        'user_email': data['user_email'],
        'scooter_id': scooter_id,
        'end': ''
    }
    return booking


@app.route('/book/<int:booking_id>/end-ride', methods=['PUT'])
def end_ride(booking_id):
    booking = {
        'id': booking_id,
        'end': 'now'
    }
    return booking


@app.route('/book/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    booking = {
        'id': booking_id,
        'title': 'title',
        'start': 'start',
        'user_email': 'user_email',
        'scooter_id': 1,
        'end': ''
    }
    return booking


@app.route('/book', methods=['GET'])
def get_all_bookings():
    return []


@app.route('/scooters/<int:scooter_id>', methods=['GET'])
def get_scooter(scooter_id):
    scooter = {
        'id': scooter_id,
        'label': 'label',
        'battery_life': 'battery_life',
        'location': 'location',
        'is_charging': 'is_charging'
    }
    return scooter


@app.route('/scooters', methods=['GET'])
def get_all_scooters():
    return []


@app.route('/scooters/<int:scooter_id>', methods=['PATCH'])
def update_scooter(scooter_id):
    return '', 204


@app.route('/scooters/<int:scooter_id>', methods=['DELETE'])
def delete_scooter(scooter_id):
    return '', 204


@app.route('/scooters', methods=['POST'])
def create_scooter():
    data = request.json
    scooter = {
        'id': 1,
        'label': data['label'],
        'battery_life': data['battery_life'],
        'location': data['location'],
        'is_charging': data['is_charging']
    }
    return scooter, 201


if __name__ == "__main__":
    app.run(debug=True, port=2050, host="api-gateway")
