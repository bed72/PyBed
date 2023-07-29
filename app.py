from sanic import Sanic

from src.schemas import graphql_app

app = Sanic("KingsCross")

app.add_route(graphql_app, "/graphql")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, access_log=False, debug=False, dev=False)
