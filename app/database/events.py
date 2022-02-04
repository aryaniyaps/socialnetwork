from app.database.core import db_session


def shutdown_session() -> None:
    """
    Shut down the database session.
    """
    db_session.remove()