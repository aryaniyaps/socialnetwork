from collections.abc import Iterable
from typing import TYPE_CHECKING, Annotated

import strawberry
from strawberry import relay
from strawberry.types import Info

if TYPE_CHECKING:
    from app.users.types import UserType
    from app.posts.types import PostType


@strawberry.type(name="Comment")
class CommentType(relay.Node):
    content: str
    owner: Annotated[
        "UserType",
        strawberry.lazy("app.users.types"),
    ]
    post: Annotated[
        "PostType",
        strawberry.lazy("app.posts.types"),
    ]

    @classmethod
    def resolve_nodes(
        cls,
        *,
        info: Info,
        node_ids: Iterable[str],
        required: bool = False,
    ):
        pass
