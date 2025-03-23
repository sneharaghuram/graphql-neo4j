import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from typing import List

# In-memory storage for users (for now)
users_db = []

# Step 1: Define a GraphQL User Type
@strawberry.type
class User:
    id: int
    name: str
    age: int

# Step 2: Define the Query for Fetching Users
@strawberry.type
class Query:
    
    @strawberry.field
    def users(self) -> List[User]:
        return users_db  # Return users from in-memory DB

# Step 3: Define a Mutation to Add Users
@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, name: str, age: int) -> User:
        new_user = User(id=len(users_db) + 1, name=name, age=age)
        users_db.append(new_user)  # Store in memory
        return new_user

# Step 4: Create the GraphQL Schema
schema = strawberry.Schema(query=Query, mutation=Mutation)

# Step 5: Set Up FastAPI with GraphQL
graphql_app = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

# # Step 6: Run the Server
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
