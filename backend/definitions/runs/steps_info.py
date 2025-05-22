from dataclasses import dataclass, field
from typing import List


@dataclass
class StepInfo:
    step_name: str
    prerequisites: List[str] = field(default_factory=list)