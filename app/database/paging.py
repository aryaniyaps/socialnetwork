from typing import TypeVar

from sqlalchemy.sql import Select
from sqlalchemy.orm import Mapped


T = TypeVar("T")


def paginate(
    statement: Select, 
    paginate_by: Mapped[T],
    after: T | None = None, 
    per_page: int | None = None,
) -> Select:
    """
    Paginate the given statement.
    :param statement: The statement to paginate.
    :param paginate_by: The attribute using which
        the given statement must be paginated.
    :param after: The attribute value after which 
        entities must be selected.
    :param per_page: The number of entities to show 
        in a page.
    :return: The paginated statement.
    """
    if after is not None:
        statement.filter(paginate_by > after)
    return statement.limit(per_page)