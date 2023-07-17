from collections.abc import Iterable
from typing import TYPE_CHECKING, Annotated

import strawberry
from strawberry import relay
from strawberry.types import Info

if TYPE_CHECKING:
    from app.users.types import UserType
    from app.comments.types import CommentType


@strawberry.type(name="Post")
class PostType(relay.Node):
    title: str
    content: str
    owner: Annotated[
        "UserType",
        strawberry.lazy("app.users.types"),
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

    @relay.connection(
        relay.ListConnection[
            Annotated[
                "CommentType",
                strawberry.lazy("app.comments.types"),
            ],
        ]
    )
    def comments(
        self,
    ) -> Iterable[Annotated["CommentType", strawberry.lazy("app.comments.types"),],]:
        raise NotImplementedError()
