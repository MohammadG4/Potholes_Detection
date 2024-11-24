![IMG_20241124_023409](https://github.com/user-attachments/assets/8a9b65f6-20f2-44f2-8ed0-06c2d07e6eb3)
# Pothole Detection System 🚧

An efficient, economical, and AI-driven solution to improve road safety by detecting potholes in real time.

---

## 📜 Table of Contents

- About the Project
- Key Features
- Installation
- Usage
- Project Structure
- Dataset
- Future Enhancements
- Contributing
- License
- Acknowledgments

---

## 🛠 About the Project

This project leverages YOLOv11 for pothole detection and MiDaS for depth estimation to provide a cost-effective 
alternative to expensive stereo camera systems used in vehicles like Tesla. The system alerts drivers to upcoming 
potholes and logs data about pothole dimensions for further analysis. By addressing road safety issues, this tool 
provides an economical way to enhance transportation infrastructure.

---

## 🌟 Key Features

- High-Accuracy Detection: Utilizes YOLOv11(nano) to detect potholes with precision in real-time.
- Pothole Dimensions: Measures the height, width, and depth of potholes using MiDaS depth estimation.
- Driver Alerts: Warns drivers of approaching potholes to improve road safety.
- Cost-Effective Solution: Eliminates the need for stereo cameras, making it an affordable alternative for wider adoption.
- Data Logging: Stores pothole dimensions in a CSV file for analysis and reporting.
- Visual Demonstrations: Includes videos of pothole detection and depth estimation results.

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- YOLO model weights (`best2.pt`) downloaded and placed in the root directory
- Required Python libraries (listed in `requirements.txt`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pothole-detection.git
   ```
2. Navigate to the project folder:
   ```bash
   cd pothole-detection
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🖥 Usage

1. To run pothole detection:
   ```bash
   python main.py --input path/to/video.mp4
   ```
2. To visualize depth estimation using MiDaS:
   ```bash
   python midas_depth.py --input path/to/video.mp4
   ```

Results will be saved as videos in the project directory.

---

## 📂 Project Structure

```
pothole-detection/
├── README.md
├── best2.pt                  # YOLO model weights
├── df_mean.csv               # Generated dataset
├── main.py                   # Pothole detection script
├── midas_depth.py            # Depth estimation script
├── loss_graph.png            # Training loss graph
├── pothole_detection_demo.mp4
├── midas_depth_demo.mp4
└── datasets/
    └── potholes_data.csv     # Final pothole dimensions dataset
```

---

## 📊 Dataset

The project outputs a dataset containing pothole dimensions (height, width, depth). Example structure:

| Height (pixels) | Width (pixels) | Depth (meters) |
|-----------------|----------------|----------------|
| 50              | 120            | 0.25           |
| 45              | 115            | 0.20           |

This data can be used for further research or infrastructure planning.

---

## 🔮 Future Enhancements

- Geotagging: Integrate GPS functionality to record pothole locations.
- Real-Time Deployment: Optimize the model for edge devices like Raspberry Pi for live detection.
- Enhanced Data Collection: Add road condition analytics based on collected data.
- Automated Repair Integration: Collaborate with road repair systems for automatic pothole repairs.

---

## 🤝 Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature/new-feature
   ```
5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of the license.

---

## 🙌 Acknowledgments

- YOLO for object detection.
- MiDaS for depth estimation.
- Inspiration from the open-source community for best practices and code structure.

---
