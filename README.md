# Math API

**Technologies used:** 

- Python
- Flask
- **Docker & Docker compose:**

Used to containerise the application for the deployment

**How to run?**

**Pre\-requisite:**

Install the docker & docker compose from this [link](https://docs.docker.com/get-docker/)

**Run the command**

```
docker-compose up –build
```

This will run the docker container with the math\_api service. 

**API Calls:**

```
# Get Minimum
curl -X POST -H "Content-Type: application/json" \
    -d '{"values": [5,3,4,1,10,50,-500,-20], "quantifier": 3 }' \
    http://127.0.0.1:5000/api/v1/min

# Get Maximum 
curl -X POST -H "Content-Type: application/json" \
    -d '{"values": [5,3,4,1,10,50,-500,-20], "quantifier": 3 }' \
    http://127.0.0.1:5000/api/v1/max

# Get Percentile
curl -X POST -H "Content-Type: application/json" \
    -d '{"values": [5,3,4,1,10,50,-500,-20], "quantifier": 75 }' \
    http://127.0.0.1:5000/api/v1/percentile

# Get Median
curl -X POST -H "Content-Type: application/json" \
    -d '{"values": [5,3,4,1,10,50,-500,-20]}' \
    http://127.0.0.1:5000/api/v1/median

# Get Average
curl -X POST -H "Content-Type: application/json" \
    -d '{"values": [5,3,4,1,10,50,-500,-20]}' \
    http://127.0.0.1:5000/api/v1/average

```

**API Endpoints:**

**POST /api/v1/min**

**Payload**

```
{
    "values": [5,3,4,1,10,50,-500,-20],
    "quantifier": 3
}
```

**Response**

```
{
    "min": [
        -500,
        -20,
        1
    ],
    "status": "success"
}
```

**POST /api/v1/max**

**Payload:**

```
{
    "values": [5,3,4,1,10,50,-500,-20],
    "quantifier": 3
}
```

**Response**

```
{
    "max": [
        50,
        10,
        5
    ],
    "status": "success"
}
```

**POST /api/v1/median**

**Payload**

```
{
    "values": [5,3,4,1,10,50,-500,-20]
}
```

**Response**

```
{
    "median": 3.5,
    "status": "success"
}
```

**POST /api/v1/percentile**

**Example Payload**

```
{
    "values": [5,3,4,1,10,50,-500,-20],
    "quantifier": 75
}
```

**Response**

```
{
    "percentile": 5,
    "status": "success"
}
```

**POST /api/v1/average**

**Example Payload**

```
{
    "values": [5,3,4,1,10,50,-500,-20]
}
```

**Response**

```
{
    "average": -55.875,
    "status": "success"
}
```
