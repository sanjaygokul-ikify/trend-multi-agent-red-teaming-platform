import unittest
from packages.core import ThreatGroup, AttackVector, TargetState
from packages.core.exceptions import InvalidThreatGroupError, InvalidAttackVectorError

class TestCore(unittest.TestCase):
    def test_threat_group(self):
        threat_group = ThreatGroup('Test Threat Group', 'Test threat group description')
        self.assertEqual(threat_group.name, 'Test Threat Group')
        self.assertEqual(threat_group.description, 'Test threat group description')

    def test_attack_vector(self):
        attack_vector = AttackVector('Test Attack Vector', 'Test attack vector description')
        self.assertEqual(attack_vector.name, 'Test Attack Vector')
        self.assertEqual(attack_vector.description, 'Test attack vector description')

    def test_target_state(self):
        target_state = TargetState('Test Target State', 'Test target state description')
        self.assertEqual(target_state.name, 'Test Target State')
        self.assertEqual(target_state.description, 'Test target state description')

    def test_invalid_threat_group(self):
        with self.assertRaises(InvalidThreatGroupError):
            ThreatGroup('Invalid Threat Group', None)

    def test_invalid_attack_vector(self):
        with self.assertRaises(InvalidAttackVectorError):
            AttackVector('Invalid Attack Vector', None)