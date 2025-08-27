from dataclasses import dataclass
from typing import List


@dataclass
class Filters:
    keep: List[str]
    drop: List[str]
