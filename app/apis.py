from typing import Optional

from app.models import *


class API:
    def login(self, username: str, password: str) -> Optional[User]:
        """로그인을 시도한다.

        성공하면 User 객체를 반환한다.
        실패하면 None을 반환한다.
        """
        raise NotImplementedError

    def logout(self) -> None:
        """로그아웃을 시도한다."""
        raise NotImplementedError

    def register(self, username: str, password: str) -> Optional[User]:
        """회원가입을 시도한다.

        성공하면 User 객체를 반환한다.
        실패하면 None을 반환한다.
        """
        raise NotImplementedError


def _make_api() -> API:
    return API()


api_client = _make_api()
