from src.config import LINE_POSITION, CLASS_NAMES

class VehicleCounter:
    def __init__(self):
        self.counted_ids = set()

        # 🔥 Class-wise counts
        self.class_counts = {name: 0 for name in CLASS_NAMES}

    def update(self, detections):
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            track_id = det["id"]
            cls_id = det["class"]

            center_y = (y1 + y2) // 2

            if track_id == -1:
                continue

            if center_y > LINE_POSITION and track_id not in self.counted_ids:
                self.counted_ids.add(track_id)

                class_name = CLASS_NAMES[cls_id]
                self.class_counts[class_name] += 1

        return self.class_counts