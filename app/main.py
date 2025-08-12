# app/main.py

from fastapi import FastAPI
from ariadne import QueryType, MutationType, gql, make_executable_schema
from ariadne.asgi import GraphQL
from app.resolvers import (
    resolve_hello,
    resolve_baby_health_advice,
    resolve_add_baby_profile,
    resolve_all_babies
)
from app.models import create_db_and_tables

# Load schema
type_defs = gql(open("app/schema.graphql").read())

# Setup GraphQL
query = QueryType()
query.set_field("hello", resolve_hello)
query.set_field("babyHealthAdvice", resolve_baby_health_advice)
query.set_field("allBabies", resolve_all_babies)

mutation = MutationType()
mutation.set_field("addBabyProfile", resolve_add_baby_profile)

schema = make_executable_schema(type_defs, [query, mutation])

# 👇 Define FastAPI app BEFORE using decorators
app = FastAPI()

# 👇 CORS middleware (optional but useful for frontend)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or use ["http://localhost:PORT"] for safety
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👇 Startup event to create DB tables
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# 👇 Mount GraphQL route
app.mount("/graphql", GraphQL(schema, debug=True))
