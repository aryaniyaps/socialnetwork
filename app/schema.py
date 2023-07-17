from strawberry import Schema
from strawberry.tools import merge_types

from app.base.queries import BaseQuery
from app.comments.queries import CommentQuery
from app.posts.queries import PostQuery
from app.users.queries import UserQuery


schema = Schema(
    query=merge_types(
        name="Query",
        types=(
            BaseQuery,
            CommentQuery,
            PostQuery,
            UserQuery,
        ),
    )
)
