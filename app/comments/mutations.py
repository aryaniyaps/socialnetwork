import strawberry
from strawberry.types import Info
from strawberry.field_extensions import InputMutationExtension

from .types import CommentType


@strawberry.type
class CommentMutation:
    @strawberry.mutation(extensions=[InputMutationExtension()])
    def create_comment(self, info: Info, content: str, post_id: str) -> CommentType:
        raise NotImplementedError()
