from src.config import CLASS_NAMES
import cv2
import numpy as np

def draw_boxes(frame, detections):
    for det in detections:
        x1, y1, x2, y2 = det["bbox"]
        cls_id = det["class"]
        track_id = det["id"]

        label = f"{CLASS_NAMES[cls_id]} ID:{track_id}"

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, label, (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)


def draw_line(frame, line_position):
    cv2.line(frame, (0, line_position), (frame.shape[1], line_position),
             (0, 0, 255), 2)


# SHOW CLASS-WISE COUNT
def draw_count(frame, class_counts):
    y_offset = 50

     # Total count
    total = sum(class_counts.values())
    cv2.putText(frame, f"Total Vehicles: {total}", (50, y_offset),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

    y_offset += 40

    for cls, count in class_counts.items():
        text = f"{cls}: {count}"
        cv2.putText(frame, text, (50, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
        y_offset += 30

def draw_speed_direction(frame, detections, speeds, directions):
    for det in detections:
        track_id = det["id"]
        x1, y1, x2, y2 = det["bbox"]

        if track_id in speeds:
            speed = int(speeds[track_id])
            direction = directions.get(track_id, "")

            text = f"{speed}km/h {direction}"
            cv2.putText(frame, text, (x1, y2+20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 2)


def draw_heatmap(frame, heatmap):
    heatmap_norm = cv2.normalize(heatmap, None, 0, 255, cv2.NORM_MINMAX)
    heatmap_uint8 = heatmap_norm.astype(np.uint8)

    heatmap_color = cv2.applyColorMap(heatmap_uint8, cv2.COLORMAP_JET)

    overlay = cv2.addWeighted(frame, 0.7, heatmap_color, 0.3, 0)
    return overlay

def draw_decision(frame, density, signal_time, priority):
    cv2.putText(frame, f"Density: {density}", (400,50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

    cv2.putText(frame, f"Signal Time: {signal_time}s", (400,80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

    cv2.putText(frame, f"Priority: {priority}", (400,110),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)