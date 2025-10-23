from dataclasses import dataclass
from typing import Optional


@dataclass
class Style:
    id: int
    color: Optional[str] = None
    size: Optional[str] = None
    inherits: Optional[int] = None
