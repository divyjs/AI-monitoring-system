import numpy as np
import cv2
import time

class TrafficAnalytics:
    def __init__(self):
        self.prev_positions = {}   # id -> (x, y)
        self.prev_times = {}       # id -> time
        self.speeds = {}          # id -> speed
        self.directions = {}      # id -> direction

        # Heatmap
        self.heatmap = None

    def initialize_heatmap(self, frame):
        if self.heatmap is None:
            self.heatmap = np.zeros((frame.shape[0], frame.shape[1]), dtype=np.float32)

    def update(self, detections, frame):
        self.initialize_heatmap(frame)

        current_time = time.time()

        for det in detections:
            track_id = det["id"]
            x1, y1, x2, y2 = det["bbox"]

            if track_id == -1:
                continue

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            self.heatmap *= 0.95
            # 🔥 HEATMAP UPDATE
            cv2.circle(self.heatmap, (cx, cy), 15, 1, -1)
            # 🔥 SPEED + DIRECTION
            if track_id in self.prev_positions:
                px, py = self.prev_positions[track_id]
                dt = current_time - self.prev_times[track_id]

                distance = np.sqrt((cx - px)**2 + (cy - py)**2)

                if dt > 0:
                    speed_px = distance / dt
                    PIXEL_TO_METER = 0.05   # adjust if needed
                    speed_mps = speed_px * PIXEL_TO_METER
                    speed_kmh = speed_mps * 3.6

                    self.speeds[track_id] = speed_kmh

                # Direction
                if cx > px:
                    self.directions[track_id] = "Right"
                else:
                    self.directions[track_id] = "Left"

            self.prev_positions[track_id] = (cx, cy)
            self.prev_times[track_id] = current_time

        return self.speeds, self.directions, self.heatmap