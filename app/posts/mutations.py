import strawberry
from strawberry.types import Info
from strawberry.field_extensions import InputMutationExtension

from .types import PostType


@strawberry.type
class PostMutation:
    @strawberry.mutation(extensions=[InputMutationExtension()])
    def create_post(self, info: Info, title: str, content: str) -> PostType:
        raise NotImplementedError()
