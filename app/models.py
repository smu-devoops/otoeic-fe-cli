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


@dataclasses.dataclass(frozen=True)
class WordDTO:
    id: typing.Optional[int] = None
    english: str
    korean: str
    type: str
    level: int
    date_modified: datetime.datetime = None
    date_created: datetime.datetime = None
    user_created: UserDTO = None


@dataclasses.dataclass(frozen=True)
class ExamDTO:
    id: typing.Optional[int] = None
    level: int
    questions: int
    is_ranked: bool
    point: typing.Optional[int] = None
    date_created: typing.Optional[datetime.datetime] = None
    date_submitted: typing.Optional[datetime.datetime] = None


@dataclasses.dataclass
class QuestionDTO:
    id: typing.Optional[int] = None
    eng: typing.Optional[str] = None
    kor: str = None
    type: str = None
    answer: typing.Optional[str] = None
    is_correct: typing.Optional[bool] = None
