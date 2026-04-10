import streamlit as st
import cv2
import tempfile

from src.detector import Detector
from src.counter import VehicleCounter
from src.analytics import TrafficAnalytics
from src.decision import TrafficDecision
from src.utils import draw_boxes, draw_line, draw_count, draw_speed_direction, draw_heatmap, draw_decision
from src.config import LINE_POSITION

st.set_page_config(layout="wide")
st.title("🚦 AI Traffic Monitoring System")

uploaded_file = st.file_uploader("Upload a traffic video", type=["mp4", "avi"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    cap = cv2.VideoCapture(tfile.name)

    detector = Detector()
    counter = VehicleCounter()
    analytics = TrafficAnalytics()
    decision = TrafficDecision()

    stframe = st.empty()
    col1, col2 = st.columns(2)

    total_placeholder = col1.empty()
    density_placeholder = col1.empty()

    class_placeholder = col2.empty()
    direction_placeholder = col2.empty()

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

        # 🔥 Direction stats
        left_count = sum(1 for d in directions.values() if d == "Left")
        right_count = sum(1 for d in directions.values() if d == "Right")

        # 🔥 Update dashboard
        total_placeholder.metric("Total Vehicles", total)

        density_placeholder.markdown(f"""
        ### 🚦 Traffic Status
        - Density: **{density}**
        - Signal Time: **{signal_time}s**
        - Priority: **{priority}**
        """)

        class_placeholder.markdown("### 🚗 Class-wise Count")
        class_placeholder.table(class_counts)

        direction_placeholder.markdown(f"""
        ### ↔️ Direction Count
        - Left: **{left_count}**
        - Right: **{right_count}**
        """)

        draw_boxes(frame, detections)
        draw_line(frame, LINE_POSITION)
        draw_count(frame, class_counts)
        draw_speed_direction(frame, detections, speeds, directions)
        draw_decision(frame, density, signal_time, priority)

        frame = draw_heatmap(frame, heatmap)

        # Convert BGR → RGB for Streamlit
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        stframe.image(frame)

    cap.release()

    st.success("Processing Complete ✅")