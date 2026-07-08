import logging
from packages.core.engine import ThreatGroupCoordinator
logger = logging.getLogger(__name__)

class RuntimeExecutor:
    def __init__(self, threat_group_coordinator: ThreatGroupCoordinator):
        self.threat_group_coordinator = threat_group_coordinator

    def execute(self):
        logger.info('Executing threat group coordinator')
        self.threat_group_coordinator.coordinate_attack()
        logger.info('Threat group coordinator execution completed')

    def track_target_state(self):
        logger.info('Tracking target state')
        self.threat_group_coordinator.track_target_state()
        logger.info('Target state tracking completed')