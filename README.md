![image](https://github.com/user-attachments/assets/b8c5ec3a-be86-426e-984d-a97b9c538c9d)

# [Redis](https://redis.io/docs/latest/)
Redis is an open-source, in-memory data structure store, commonly used as a database, cache, or message broker, known for its speed and efficiency due to storing data in RAM

The name **Redis** stands for **"`Re`mote `Di`ctionary `S`erver"** because it was originally designed as a fast, in-memory key-value store that behaves like a dictionary (hash map).  

It was created by **Salvatore Sanfilippo** in 2009 to improve performance in his own projects but later became a widely used **NoSQL database**, supporting various data structures like strings, lists, sets, and more.

**Reference Video**
- [Redis | Cache Aside Pattern | Parottasalna | Tamil - 15 Min Video](https://www.youtube.com/watch?v=tf46FmXho6w)

### Key Characteristics:

- **In-Memory Data Store:**
    - Redis stores data in RAM (Random Access Memory), providing significantly faster access times compared to disk-based 
- **Key-Value Store:**
    - It operates as a key-value store, where data is organized into key-value pairs. 
- **NoSQL Database:**
    - Redis is a NoSQL database, meaning it doesn't adhere to the strict relational database model. 
- **Versatile Usage:**
    - `Cache`: To store frequently accessed data for faster retrieval. 
    - `Database`: As a primary database or a secondary database for specific use cases. 
    - `Message Broker`: For real-time communication and event-driven architectures. 
- **Data Structures:**
    - Redis supports various data structures, including strings, hashes, lists, sets, sorted sets, bitmaps, streams, and geospatial indexes.

### Use Cases:
- `Caching`: Storing frequently accessed data to reduce database load and improve performance. 
- `Session Management`: Storing user session data for web applications. 
- `Real-time Analytics`: Processing and storing real-time data streams. 
- `Leaderboard Systems`: Maintaining and updating leaderboards in online games. 
- `Message Queues`: Facilitating asynchronous communication between different parts of an application. 
- `Geospatial Applications`: Storing and querying location data. 
- `Content Delivery Networks (CDNs)`: Storing cached content for faster delivery to users.


# [Quick Start | Docker](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/docker/)

Ensure the docker is installed in your machine. For more info about the [redis-stack](https://hub.docker.com/r/redis/redis-stack). 

### Step 1 : Clone The Repo

```
git clone https://github.com/Antony-M1/docker-redis.git
```
```
cd docker-redis
```

### Step 2: Run the docker-compose.yml file

```
docker compose up -d
```

Go To: [localhost:5540](http://localhost:5540)

## Notes
 There are two components in the `docker-compose.yml` file. One is **Redis**, which is running on port `6379`, and the other is **RedisInsight**, a GUI for Redis, which is running at [localhost:8001](http://localhost:8001).

## [Redis CLI](https://redis.io/docs/latest/develop/tools/cli/)
- Overview of redis-cli, the Redis command line interface
- In interactive mode, redis-cli has basic line editing capabilities to provide a familiar typing experience.

Use the below commands to access the redis cli from the docker container.
```
docker exec -it redis-stack redis-cli
```

<details>
    <summary><b>Some sample commands to use in the redis-cli</b></summary>

To Select the database
```
SELECT 0
```

To set the information in the redis database

Syntax: `SET <KEY> <VALUE>`
```
SET name "John Doe"
```

To Get the information

Syntax: `GET <KEY>`
```
GET name
```
</details>


