from packages.core.types import ThreatGroup, AttackVector, TargetState
from packages.core.exceptions import InvalidThreatGroupError, InvalidAttackVectorError
from . import orchestration

class Orchestrator:
    def __init__(self, threat_group: ThreatGroup):
        self.threat_group = threat_group

    def orchestrate(self):
        orchestration.orchestrate(self.threat_group)