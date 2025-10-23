from dataclasses import dataclass
from typing import Optional


@dataclass
class Text:
    id: int
    style: int
    content: str
    section: int
    link: Optional[int] = None
