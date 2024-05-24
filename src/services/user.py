from __future__ import annotations

import dataclasses
import typing


class UserAlreadyExistsException(Exception):
    pass


@dataclasses.dataclass
class User:
    id: int
    username: str
    level: int
    is_admin: bool
    streak: int
    streak_freeze_amount: int
    is_streak_freeze_activated: bool
    point: int


class UserService:
    def login(self, username: str, password: str) -> typing.Optional[User]:
        # TODO
        ...

    def logout(self) -> None:
        # TODO
        ...

    def signup(self, username: str, password: str):
        # TODO
        if ...:
            raise UserAlreadyExistsException
        ...

    def current_user(self) -> User:
        # TODO
        ...


user_service = UserService()
