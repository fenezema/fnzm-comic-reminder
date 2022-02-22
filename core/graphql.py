from ariadne import load_schema_from_path, make_executable_schema
from .querybind import bindQueries
from .mutationbind import bindMutations

def buildGraphQLSchema():
    query = bindQueries()
    mutation = bindMutations()
    type_defs = load_schema_from_path("schema.graphql")
    return make_executable_schema(
        type_defs, query, mutation
    )