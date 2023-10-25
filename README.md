# Distributed Applications Course
#### Technical University of Moldova 2023

## Scooters Renting service

### How to run?
Clone the repo, cd to the root of the project and run:
```commandline
    docker compose up --build
```

### Assess Application Suitability

In a scooter rental service, application load can vary significantly based on factors like location, 
time of day, and special events. Microservices enable to scale individual components independently, 
ensuring that the resources are allocated efficiently. For example, the booking service can be scale
during peak hours while keeping other services running at their usual capacity, and due to the multitude of 
data sent by sensors, the scooters management can be scaled a lot more.

### Service Boundaries

The application itself will be composed of two microservices:

 - **Booking Service** - responsible for handling bookings CRUD operations and storing data about the users
 - **ScootersManagement Service** - responsible for scooters CRUD operations, storing data from GPS and
battery sensors

![ArchitectureDiagram.jpeg](ArchitectureDiagram.jpeg)

### Booking Service endpoints

1. **POST**: `/book/scooters/{id}`
Create a booking for a scooter with a specific id

Request body:
```JSON
{
  "title": "Ride 1",
  "start": "2023-25-12 23:50:55",
  "user_email": "email@test.com"
}
```
Response body:
```JSON
{
  "id": 1,
  "start": "2023-25-12 23:50:55",
  "user_email": "email@test.com",
  "title": "Ride 1",
  "scooter_id": "2",
  "end": ""
}
```

2. **PATCH**: `/book/{id}/end-ride` End booking by id

No Request Body

Response body:
```JSON
{
  "id": 1,
  "title": "Ride 1",
  "start": "2023-25-12 23:50:55",
  "user_email": "email@test.com",
  "scooter_id": "2",
  "end": "2023-26-12 01:52:51"
}
```

3. GET `/book/{id}` Show booking details by id

No Request Body

Response body:
```JSON
{
  "id": 1,
  "title": "Ride 1",
  "start": "2023-25-12 23:50:55",
  "user_email": "email@test.com",
  "scooter_id": "2",
  "end": "2023-26-12 01:52:51"
}
```
4. **GET** `/book` Get all bookings, may include query params for filtering purposes

No Request Body

Response body:
```JSON
[
  {
    "id": 1,
    "title": "Ride 1",
    "start": "2023-25-12 23:50:55",
    "user_email": "email@test.com",
    "scooter_id": "2",
    "end": "2023-26-12 01:52:51"
  },
  {
    "id": 2,
    "title": "Ride 2",
    "start": "2023-26-12 23:50:55",
    "user_email": "email@test.com",
    "scooter_id": "2",
    "end": ""
  }
]
```

### Scooters Management Service endpoints

1. **GET** `/scooters/{id}` show scooter by id

No Request Body

Response body:
```JSON
{
"id": 1,
"label": "0001",
"battery_life": "48",
"location": "52.4343242,-1.32324",
"is_charging": 1
}
```

2. **GET** `/scooters` show all scooters, may include query params for filtering

No Request Body

Response body:
```JSON
[
  {
    "id": 1,
    "label": "0001",
    "battery_life": "48",
    "location": "52.4343242,-1.32324",
    "is_charging": 1
  },
  {
    "id": 2,
    "label": "0002",
    "battery_life": "100",
    "location": "52.4341242,-1.32324",
    "is_charging": 0
  }
]
```

3. **PATCH** `/scooters/{id}` update scooters information by id

Request Body
```JSON
{
  "label": "0001",
  "battery_life": "18",
  "location": "52.4343242,-1.32324",
  "is_charging": 1
}
```

No Response body

4. **DELETE** `/scooters/{id}` delete scooter by id

No Request Bod

No Response body

5. **POST** `/scooters` create scooter

Request Body
```JSON
{
  "label": "0001",
  "battery_life": "18",
  "location": "52.4343242,-1.32324",
  "is_charging": 1
}
```

Response body
```JSON
{
  "id": 2
  "label": "0001",
  "battery_life": "18",
  "location": "52.4343242,-1.32324",
  "is_charging": 1
}
```

### Technology Stack

For the implementation, **nodeJs** will be used for creating microservices and for API Gateway and Service Discovery,
**Python** will be used. Inter services communication will be performed synchronously using **gRPC** communication,
but the client application will send basic **HTTP** requests.

### Data Management Design

Each service will operate on separate MySQL databases, to enhance performance of the system, a Redis cacheing
system will be implemented at the level of API Gateway.

### Deployment and Scaling

The services and databases will containerized using Docker, for orchestration
Kubernetes will eb used.