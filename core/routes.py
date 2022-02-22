from flask import Flask
from core.graphql import buildGraphQLSchema
from ariadne.constants import PLAYGROUND_HTML
from ariadne import graphql_sync
from flask import request, jsonify

App = Flask(__name__)
App.config["DB_PATH"] = "./db"
Schema = buildGraphQLSchema()

# GraphQL routes to serve GraphQL endpoints and GraphQL Playground
@App.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@App.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        Schema,
        data,
        context_value=request,
        debug=App.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code