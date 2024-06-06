import dataclasses
import datetime
import typing


@dataclasses.dataclass(frozen=True)
class UserDTO:
    id: int = None
    username: str = None
    level: int = None
    point: int = None
    freeze_amount: int = None
    freeze_activated: bool = None
    streak: int = None
    date_created: datetime.datetime = None
    is_staff: int = None

    def __hash__(self) -> int:
        return self.id


@dataclasses.dataclass(frozen=True)
class WordDTO:
    english: str
    korean: str
    type: str
    level: int
    id: typing.Optional[int] = None
    date_modified: datetime.datetime = None
    date_created: datetime.datetime = None
    user_created: UserDTO = None

    def __hash__(self) -> int:
        return self.id


@dataclasses.dataclass(frozen=True)
class ExamDTO:
    level: int
    questions: int
    is_ranked: bool
    id: typing.Optional[int] = None
    point: typing.Optional[int] = None
    date_created: typing.Optional[datetime.datetime] = None
    date_submitted: typing.Optional[datetime.datetime] = None

    def __hash__(self) -> int:
        return self.id


@dataclasses.dataclass
class QuestionDTO:
    kor: str = None
    type: str = None
    id: typing.Optional[int] = None
    eng: typing.Optional[str] = None
    answer_submitted: typing.Optional[str] = None
    is_correct: typing.Optional[bool] = None

    def __hash__(self) -> int:
        return self.id
