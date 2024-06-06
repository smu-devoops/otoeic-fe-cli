from __future__ import annotations

from typing import *

from app.models import *


class API:
    def __init__(self,
                 user: UserAPI = None,
                 word: WordAPI = None,
                 exam: ExamAPI = None):
        self._user = user if user is not None else UserAPI()
        self._word = word if word is not None else WordAPI()
        self._exam = exam if exam is not None else ExamAPI()

    @property
    def user(self) -> UserAPI:
        return self._user

    @property
    def word(self) -> WordAPI:
        return self._word

    @property
    def exam(self) -> ExamAPI:
        return self._exam


class UserAPI:
    def register(self, username: str, password: str) -> Optional[UserDTO]:
        """회원가입을 시도한다.

        성공하면 User 객체를 반환한다.
        실패하면 None을 반환한다.
        """
        raise NotImplementedError

    def login(self, username: str, password: str) -> Optional[UserDTO]:
        """로그인을 시도한다.

        성공하면 User 객체를 반환한다.
        실패하면 None을 반환한다.
        """
        raise NotImplementedError

    def logout(self) -> None:
        """로그아웃을 시도한다."""
        raise NotImplementedError

    def is_logged_in(self) -> bool:
        """로그인 여부를 반환한다."""
        raise NotImplementedError

    def current_user(self) -> UserDTO:
        """현재 로그인된 사용자를 반환한다."""
        raise NotImplementedError

    def update(self, user: UserDTO) -> UserDTO:
        """사용자 정보를 수정한다.

        수정된 사용자 정보를 반환한다."""
        raise NotImplementedError


class WordAPI:
    def create(self, word: WordDTO) -> WordDTO:
        """단어를 생성한다.

        WordDTO의 english, korean, type, level 필드는 필수로 설정되어있어야 한다.

        생성된 단어를 반환한다."""
        raise NotImplementedError

    def list(self, sort_by: str) -> List[WordDTO]:
        """모든 단어를 가져온다."""
        raise NotImplementedError

    def update(self, word: WordDTO) -> WordDTO:
        """단어를 수정한다.

        수정된 단어를 반환한다."""
        raise NotImplementedError

    def delete(self, word: WordDTO) -> None:
        """단어를 삭제한다."""
        raise NotImplementedError


class ExamAPI:
    def create(self, exam: ExamDTO) -> ExamDTO:
        """시험을 생성한다.

        ExamDTO의 level, questions, is_ranked 필드는 필수로 설정되어있어야 한다.

        생성된 시험을 반환한다."""
        raise NotImplementedError

    def get_questions(self, exam: ExamDTO) -> List[QuestionDTO]:
        """시험의 문제를 가져온다.

        제출된 적 없는 시험이라면, 각 문제의 실제 정답 정보는 비어있는
        QuestionDTO 객체가 리스트 형태로 반환된다."""
        raise NotImplementedError

    def submit(self, exam: ExamDTO, answers: List[QuestionDTO]) -> ExamDTO:
        """시험을 제출한다.

        시험의 점수가 반영된 ExamDTO를 반환한다."""
        raise NotImplementedError

    def list(self) -> List[ExamDTO]:
        """모든 시험을 가져온다."""
        raise NotImplementedError
