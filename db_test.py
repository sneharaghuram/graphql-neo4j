from neo4j import GraphDatabase

# Neo4j Connection Details
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

# Create a Neo4j Driver instance
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Function to run a Neo4j query
def run_query(query, parameters=None):
    with driver.session() as session:
        result = session.run(query, parameters or {})
        # Convert result to a list to prevent 'result consumed' issue
        return list(result)

# Function to close the database connection (optional)
def close_connection():
    driver.close()

# Test Query (e.g., list all nodes)
query = "MATCH (n) RETURN n LIMIT 5"  # Limit to 5 results for brevity
results = run_query(query)

# Iterate over the results
for record in results:
    print(record)

# Close the connection (optional)
close_connection()
