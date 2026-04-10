import cv2
import csv

from src.detector import Detector
from src.counter import VehicleCounter
from src.utils import draw_boxes, draw_line, draw_count
from src.analytics import TrafficAnalytics
from src.utils import draw_speed_direction, draw_heatmap, draw_decision
from src.decision import TrafficDecision
from src.config import VIDEO_PATH, OUTPUT_PATH, LINE_POSITION

def main():
    cap = cv2.VideoCapture(VIDEO_PATH)

    decision = TrafficDecision()
    detector = Detector()
    counter = VehicleCounter()
    analytics = TrafficAnalytics()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(OUTPUT_PATH, fourcc, 20.0, (640,480))

    csv_file = open("outputs/results.csv", "w", newline="")
    writer = csv.writer(csv_file)
    writer.writerow(["Class", "Count"])

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640,480))
        detections = detector.detect(frame)
        class_counts = counter.update(detections)
        speeds, directions, heatmap = analytics.update(detections, frame)

        total = sum(class_counts.values())
        density = decision.get_density_level(total)
        signal_time = decision.get_signal_time(density)
        priority = decision.decide_priority(directions)

        draw_boxes(frame, detections)
        draw_line(frame, LINE_POSITION)
        draw_count(frame, class_counts)
        draw_speed_direction(frame, detections, speeds, directions)
        draw_decision(frame, density, signal_time, priority)
        frame=draw_heatmap(frame, heatmap)
        out.write(frame)
        cv2.imshow("Traffic Monitoring", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    for cls, count in class_counts.items():
        writer.writerow([cls, count])

    csv_file.close()
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print("\nFinal Vehicle Count Summary:")
    for cls, count in class_counts.items():
        print(f"{cls}: {count}")

    print(f"\nTotal Vehicles: {sum(class_counts.values())}")
if __name__ == "__main__":
    main()