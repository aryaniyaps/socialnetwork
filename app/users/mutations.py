import strawberry
from strawberry.types import Info
from strawberry.field_extensions import InputMutationExtension

from .types import UserType


@strawberry.type
class UserMutation:
    @strawberry.mutation(extensions=[InputMutationExtension()])
    def create_user(
        self,
        info: Info,
        username: str,
        password: str,
        email: str,
        full_name: str,
    ) -> UserType:
        raise NotImplementedError()
