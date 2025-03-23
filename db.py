from neo4j import GraphDatabase

# Neo4j Connection Details
NEO4J_URI = "bolt://localhost:7687"  # Change if needed
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

# Create a Neo4j Driver instance
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Function to run a Neo4j query
def run_query(query, parameters=None):
    with driver.session() as session:
        results =  session.run(query, parameters or {})
        return list(results)


# Function to close the database connection (optional)
def close_connection():
    driver.close()
