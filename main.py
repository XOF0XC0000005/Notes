import dataclasses

@dataclasses.dataclass
class Note:
    title: str
    msg: str
    date: str