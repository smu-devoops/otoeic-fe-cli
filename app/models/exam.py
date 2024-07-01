import dataclasses
import datetime
import typing


@dataclasses.dataclass(frozen=True)
class ExamDTO(typing.Hashable):
    id: typing.Optional[int] = None
    level: int
    questions: int
    is_ranked: bool
    point: typing.Optional[int] = None
    date_created: typing.Optional[datetime.datetime] = None
    date_submitted: typing.Optional[datetime.datetime] = None

    def __hash__(self) -> int:
        return self.id
