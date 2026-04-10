import numpy as np

class SimpleTracker:
    def __init__(self):
        self.next_id = 0
        self.objects = {}  # id -> centroid

    def get_centroid(self, bbox):
        x1, y1, x2, y2 = bbox
        return ((x1 + x2)//2, (y1 + y2)//2)

    def update(self, detections):
        new_objects = {}

        for det in detections:
            bbox = det["bbox"]
            centroid = self.get_centroid(bbox)

            matched_id = None

            for obj_id, prev_centroid in self.objects.items():
                distance = np.linalg.norm(
                    np.array(centroid) - np.array(prev_centroid)
                )

                if distance < 50:  # threshold
                    matched_id = obj_id
                    break

            if matched_id is not None:
                new_objects[matched_id] = centroid
            else:
                new_objects[self.next_id] = centroid
                self.next_id += 1

        self.objects = new_objects
        return self.objects