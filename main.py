import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from typing import List
from db import run_query

# Step 1: Define a GraphQL User Type
@strawberry.type
class User:
    id: int
    name: str
    age: int

# Step 2: Define Query to Fetch Users from Neo4j
@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        query = "MATCH (u:User) RETURN u.id AS id, u.name AS name, u.age AS age"
        result = run_query(query)
        return [User(id=record["id"], name=record["name"], age=record["age"]) for record in result]

# Step 3: Define Mutation to Add Users to Neo4j
@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, name: str, age: int, id: int) -> User:
        query = """
        CREATE (u:User {id: $id, name: $name, age: $age})
        RETURN u.id AS id, u.name AS name, u.age AS age
        """
        result = run_query(query, {"name": name, "age": age, "id": id})
        record = result.single()
        return User(id=record["id"], name=record["name"], age=record["age"])

# Step 4: Create GraphQL Schema
schema = strawberry.Schema(query=Query, mutation=Mutation)

# Step 5: Set Up FastAPI with GraphQL
app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# Step 6: Run the Server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
