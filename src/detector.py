from ultralytics import YOLO
from src.config import MODEL_PATH

class Detector:
    def __init__(self):
        self.model = YOLO(MODEL_PATH)

    def detect(self, frame):
        results = self.model.track(frame, persist=True)

        detections = []

        for r in results:
            if r.boxes is None:
                continue

            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls_id = int(box.cls[0])

                # 🔥 THIS IS THE MAGIC (tracking ID)
                track_id = int(box.id[0]) if box.id is not None else -1

                detections.append({
                    "bbox": (x1, y1, x2, y2),
                    "class": cls_id,
                    "id": track_id
                })

        return detections