from dataclasses import dataclass
from typing import List

@dataclass
class ThreatGroup:
    name: str
    description: str

@dataclass
class AttackVector:
    name: str
    description: str

@dataclass
class TargetState:
    name: str
    description: str