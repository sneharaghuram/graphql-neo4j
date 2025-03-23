## GraphQL + Neo4j Project

This project demonstrates how to build a simple **GraphQL API** using **FastAPI**, **Strawberry**, and **Neo4j**. The API allows you to interact with a Neo4j database and perform basic operations such as querying and adding `Person` records.

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python 3.6+ based on standard Python-type hints.
- **Strawberry**: A Python library for building GraphQL APIs.
- **Neo4j**: A graph database used to store and query data.
- **Uvicorn**: ASGI server to run the FastAPI app.
- **GraphQL**: A query language for APIs that allows clients to request exactly the data they need, making it efficient for interacting with complex data structures like those in a graph database.

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- **Python 3.6+**
- **Docker** (Optional but recommended for running Neo4j)
- **Neo4j Desktop** (An alternative to Docker if you prefer a graphical interface)

### Install Dependencies

First, clone the repository:

```bash
git clone https://github.com/your-username/graphql-neo4j-project.git
cd graphql-neo4j-project
```

Install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

### Option 1: Run Neo4j Using Docker

You can use **Docker** to run Neo4j locally. This is the easiest way to get Neo4j up and running without needing to install it manually.

1. Create a `docker-compose.yml` file in your project folder:

   ```yaml
   version: "3"
   services:
     neo4j:
       image: neo4j:latest
       environment:
         - NEO4J_AUTH=neo4j/password # Replace with your desired username and password
       ports:
         - "7474:7474" # HTTP port for Neo4j Browser
         - "7687:7687" # Bolt protocol port for connections
   ```

2. Run Neo4j in a Docker container:

   ```bash
   docker-compose up
   ```

   Neo4j will now be accessible at `http://localhost:7474` (Neo4j Browser) and will be running with the Bolt protocol on `bolt://localhost:7687`.

### Option 2: Use Neo4j Desktop (Alternative Solution)

If you prefer using a graphical interface, you can install **Neo4j Desktop**.

1. Download and install **Neo4j Desktop** from [Neo4j’s official website](https://neo4j.com/download/).
2. Create a new project in Neo4j Desktop and start a new database instance.
3. Once Neo4j is running, update your `db.py` file to point to the Neo4j instance running on your machine (typically `bolt://localhost:7687`).

### Update Neo4j Connection in `db.py`

Regardless of whether you use Docker or Neo4j Desktop, you'll need to configure the Neo4j connection details in your `db.py` file:

```python
from neo4j import GraphDatabase

def get_driver():
    # Replace with your Neo4j connection URI and credentials
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "your_password"
    driver = GraphDatabase.driver(uri, auth=(user, password))
    return driver

def run_query(query, parameters=None):
    driver = get_driver()
    session = driver.session()
    result = session.run(query, parameters or {})
    return result
```

### Run the Application

Once everything is set up, you can run the FastAPI application:

```bash
uvicorn main:app --reload
```

The server will run on `http://localhost:8000`. You can navigate to the `/graphql` endpoint in your browser to access the GraphQL Playground.

## API Overview

### GraphQL Queries

#### `persons`

- **Description**: Fetch all persons from the database.
- **Query**:
  ```graphql
  query {
    persons {
      id
      name
      age
    }
  }
  ```
- **Response**:
  ```json
  {
    "data": {
      "persons": [
        {
          "id": 1,
          "name": "John Doe",
          "age": 30
        },
        {
          "id": 2,
          "name": "Jane Doe",
          "age": 25
        }
      ]
    }
  }
  ```

### GraphQL Mutations

#### `add_person`

- **Description**: Adds a new person to the Neo4j database.
- **Mutation**:
  ```graphql
  mutation {
    addPerson(name: "John Smith", age: 35, id: 3) {
      id
      name
      age
    }
  }
  ```
- **Response**:
  ```json
  {
    "data": {
      "addPerson": {
        "id": 3,
        "name": "John Smith",
        "age": 35
      }
    }
  }
  ```

### Available Endpoints

- **GraphQL Playground**: `http://localhost:8000/graphql`
- **GraphQL API**: `http://localhost:8000/graphql`

## Folder Structure

```
graphql-neo4j-project/
│
├── db.py              # Contains the logic for interacting with the Neo4j database.
├── main.py            # FastAPI app setup and GraphQL schema definition.
├── requirements.txt   # Python dependencies.
└── README.md          # Project documentation.
```
