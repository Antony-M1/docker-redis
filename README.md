![image](https://github.com/user-attachments/assets/b8c5ec3a-be86-426e-984d-a97b9c538c9d)

# [Redis](https://redis.io/docs/latest/)
Redis is an open-source, in-memory data structure store, commonly used as a database, cache, or message broker, known for its speed and efficiency due to storing data in RAM

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


# Quick Start | Docker

Before running the docker the below commands ensure that docker is installed and running in your machine 

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
 There are two components in the `docker-compose.yml` file. One is **Redis**, which is running on port `6379`, and the other is **RedisInsight**, a GUI for Redis, which is running at [localhost:5540](http://localhost:5540).
