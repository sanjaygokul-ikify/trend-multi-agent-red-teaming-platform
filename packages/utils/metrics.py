class Metrics:
    def __init__(self):
        self.metrics = {}

    def add_metric(self, metric_name: str, value: int):
        self.metrics[metric_name] = value

    def get_metric(self, metric_name: str) -> int:
        return self.metrics.get(metric_name, 0)