from typing import List
from typing import Optional

from app.models import *


class UserAPI:
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


class WordAPI:
    def create(self, word: Word) -> Word:
        """단어를 생성한다.

        생성된 단어를 반환한다."""
        raise NotImplementedError

    def get(self, id: int) -> Word:
        """단어를 가져온다."""
        raise NotImplementedError

    def all(self) -> List[Word]:
        """모든 단어를 가져온다."""
        raise NotImplementedError

    def update(self, word: Word) -> Word:
        """단어를 수정한다.

        수정된 단어를 반환한다."""
        raise NotImplementedError

    def delete(self, id: int) -> None:
        """단어를 삭제한다."""
        raise NotImplementedError