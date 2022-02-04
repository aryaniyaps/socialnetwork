from starlette.applications import Starlette
from strawberry.asgi import GraphQL

from app.config import DEBUG
from app.schema import schema


def create_app() -> Starlette:
    """
    Initialize an app instance.

    :return: The created app.
    """
    app = Starlette(debug=DEBUG)
    configure_routes(app)
    configure_middleware(app)
    configure_event_handlers(app)
    return app


def configure_routes(app: Starlette) -> None:
    """
    Configure routes for the app.

    :param app: The app instance.
    """
    app.add_route(
        path="/graphql",
        route=GraphQL(
            schema=schema, 
            graphiql=True, 
            debug=DEBUG,
        ),
    )


def configure_middleware(app: Starlette) -> None:
    """
    Configure middleware for the app.
    
    :param app: The app instance.
    """
    pass


def configure_event_handlers(app: Starlette) -> None:
    """
    Configure event handlers for the app.

    :param app: The app instance.
    """
    pass