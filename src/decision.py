class TrafficDecision:
    def __init__(self):
        pass

    def get_density_level(self, total_count):
        if total_count < 10:
            return "LOW"
        elif total_count < 25:
            return "MEDIUM"
        else:
            return "HIGH"
    
    def get_signal_time(self, density):
        if density == "LOW":
            return 15
        elif density == "MEDIUM":
            return 30
        else:
            return 60
        
    def decide_priority(self, directions):
        left_count = sum(1 for d in directions.values() if d == "Left")
        right_count = sum(1 for d in directions.values() if d == "Right")

        if left_count > right_count:
            return "LEFT"
        else:
            return "RIGHT"    