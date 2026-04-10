🚦 AI Traffic Monitoring System

An intelligent traffic monitoring and analytics system built using *YOLOv8, OpenCV, and Streamlit*.  
The system detects vehicles in real-time, tracks them, estimates speed, analyzes traffic density, and makes smart traffic signal decisions.

---


## 🎯 Features

* 🚗 Vehicle Detection using YOLOv8  
* 📊 Vehicle Counting (Car, Bus, Truck, Motorcycle, etc.)  
* 🧭 Direction Detection (Left / Right movement)  
* ⚡ Speed Estimation (km/h)  
* 🔥 Traffic Density Analysis  
* 📍 Traffic Heatmap Visualization  
* 🚦 Smart Traffic Signal Decision System  
* 📈 Live Analytics Dashboard using Streamlit  

---

## 🧠 System Architecture
# 🚦 AI Traffic Monitoring System

An intelligent traffic monitoring and analytics system built using *YOLOv8, OpenCV, and Streamlit*.  
The system detects vehicles in real-time, tracks them, estimates speed, analyzes traffic density, and makes smart traffic signal decisions.

---


## 🎯 Features

* 🚗 Vehicle Detection using YOLOv8  
* 📊 Vehicle Counting (Car, Bus, Truck, Motorcycle, etc.)  
* 🧭 Direction Detection (Left / Right movement)  
* ⚡ Speed Estimation (km/h)  
* 🔥 Traffic Density Analysis  
* 📍 Traffic Heatmap Visualization  
* 🚦 Smart Traffic Signal Decision System  
* 📈 Live Analytics Dashboard using Streamlit  

---

## 🧠 System Architecture
Video Input
↓
YOLO Vehicle Detection
↓
Object Tracking
↓
Vehicle Counting
↓
Speed Estimation
↓
Traffic Density Analysis
↓
Smart Traffic Signal Decision
↓
Streamlit Dashboard

## 🛠️ Tech Stack

*AI / Computer Vision*
- YOLOv8
- OpenCV
- NumPy

*Web Interface*
- Streamlit

*Deployment*
- Hugging Face Spaces (Docker)

*Programming Language*
- Python

---

## 📂 Project Structure
traffic-monitoring-ai
│
├── app.py # Streamlit UI application
├── requirements.txt # Python dependencies
├── Dockerfile # Deployment configuration
├── README.md
│
├── src/
│ ├── detector.py # YOLO object detection
│ ├── counter.py # Vehicle counting logic
│ ├── analytics.py # Speed & direction detection
│ ├── decision.py # Smart traffic decision logic
│ ├── utils.py # Visualization utilities
│ └── config.py # Project configuration
│
├── models/
│ └── best.pt # Trained YOLO model
│
├── data/ # Sample input videos
└── outputs/ # Generated outputs
