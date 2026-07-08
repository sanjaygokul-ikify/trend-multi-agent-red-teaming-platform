import argparse
from packages.core import ThreatGroup, AttackVector, TargetState
from services.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(description='Multi-Agent Red Teaming Platform')
    parser.add_argument('--threat-group', type=str, help='Threat group name')
    parser.add_argument('--attack-vector', type=str, help='Attack vector name')
    parser.add_argument('--target-state', type=str, help='Target state name')
    args = parser.parse_args()

    threat_group = ThreatGroup(args.threat_group, 'Test threat group')
    attack_vector = AttackVector(args.attack_vector, 'Test attack vector')
    target_state = TargetState(args.target_state, 'Test target state')

    orchestrator = Orchestrator(threat_group)
    orchestrator.orchestrate()