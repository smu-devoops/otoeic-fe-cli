import dataclasses
import typing


@dataclasses.dataclass
class QuestionDTO(typing.Hashable):
    id: typing.Optional[int] = None
    eng: typing.Optional[str] = None
    kor: str = None
    type: str = None
    answer_submitted: typing.Optional[str] = None
    is_correct: typing.Optional[bool] = None

    def __hash__(self) -> int:
        return self.id
