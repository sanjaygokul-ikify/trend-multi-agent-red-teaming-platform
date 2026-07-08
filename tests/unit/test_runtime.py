import unittest
from packages.core import ThreatGroupCoordinator

class TestRuntime(unittest.TestCase):
    def test_threat_group_coordinator(self):
        threat_group = ThreatGroup('Test Threat Group', 'Test threat group description')
        coordinator = ThreatGroupCoordinator(threat_group)
        self.assertEqual(coordinator.threat_group.name, 'Test Threat Group')