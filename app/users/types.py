from collections.abc import Iterable
from typing import TYPE_CHECKING, Annotated

import strawberry
from strawberry import relay
from strawberry.types import Info

if TYPE_CHECKING:
    from app.posts.types import PostType


@strawberry.type(name="User")
class UserType(relay.Node):
    username: str
    full_name: str
    email: str
    avatar_url: str

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
                "PostType",
                strawberry.lazy("app.posts.types"),
            ]
        ]
    )
    def posts(
        self,
    ) -> Iterable[Annotated["PostType", strawberry.lazy("app.posts.types"),],]:
        raise NotImplementedError()
