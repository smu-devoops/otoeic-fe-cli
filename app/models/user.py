import dataclasses
import datetime
import typing


@dataclasses.dataclass(frozen=True)
class UserDTO(typing.Hashable):
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
