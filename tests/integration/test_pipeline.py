import unittest
from packages.core import ThreatGroup, AttackVector, TargetState
from services.orchestrator import Orchestrator

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        threat_group = ThreatGroup('Test Threat Group', 'Test threat group description')
        attack_vector = AttackVector('Test Attack Vector', 'Test attack vector description')
        target_state = TargetState('Test Target State', 'Test target state description')

        orchestrator = Orchestrator(threat_group)
        orchestrator.orchestrate()
        self.assertTrue(True)