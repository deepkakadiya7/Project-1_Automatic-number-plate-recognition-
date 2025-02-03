#  Automatic Number Plate Recognition (ANPR) Using Python and YOLOv8

## Overview

The Automatic Number Plate Recognition (ANPR) system is a powerful computer vision project designed to detect and recognize vehicle license plates using the YOLOv8 object detection model and EasyOCR for text recognition. This project has applications in traffic monitoring, toll collection systems, parking management, and security surveillance.

## Features

🚗 Vehicle Detection: Identifies vehicles in real-time video streams or static images.

📸 License Plate Detection: Accurately locates license plates using a custom-trained YOLOv8 model.

🔤 Text Recognition: Extracts license plate characters with high accuracy using EasyOCR.

🎯 Vehicle Tracking: Tracks vehicles across frames using the SORT (Simple Online and Realtime Tracking) algorithm.

⚡ Real-time Processing: Optimized for real-time video stream analysis with GPU support.

Requirements

## 🖥️ Software

Python 3.8 or later

pip (Python package manager)

## 📦 Python Libraries

ultralytics

easyocr

opencv-python

numpy

matplotlib

sort (download from the SORT repository)

## ⚙️ Hardware (Optional but Recommended)

A GPU-enabled system for faster inference and real-time performance.

## 📊 Dataset

A labeled dataset of vehicle images with annotated license plates for YOLOv8 training and testing.

## 📁 File Structure

```plaintext
automatic-number-plate-recognition-python-yolov8/
├── README.md
├── LICENSE
├── requirements.txt
├── main.py
├── util.py
├── visualize.py
├── add_missing_data.py
├── models/
│   └── yolov8_trained_model.pt
└── data/
    ├── video.mp4
    └── images/
        └── example_image.jpg
```

## 🚀 Installation

1️⃣ **Clone the Repository**

```bash
git clone https://github.com/yourusername/automatic-number-plate-recognition-python-yolov8.git
cd automatic-number-plate-recognition-python-yolov8
```

2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Install the SORT Module

Follow the instructions provided in the SORT Repository to install the module.

4️⃣ Add the YOLOv8 Model

Place your trained YOLOv8 model file (yolov8_trained_model.pt) inside the models/ directory

## ⚡ How It Works
Vehicle Detection: The pretrained YOLOv8 model identifies vehicles in images or video frames.
License Plate Detection: A custom YOLOv8 model detects license plates within the detected vehicles.
Text Recognition: EasyOCR extracts and recognizes characters from the detected license plate regions.
Visualization: Bounding boxes and recognized text are overlaid on the processed frames for easy viewing.

## 🎯 Usage
1️⃣ Run the Main Program
python main.py --input data/video.mp4
Options:

--input: Path to the input video or image file.
--output (Optional): Path to save the processed output video.

2️⃣ Visualize Intermediate Results
```bash
python visualize.py
```

## 📊 Example Outputs
Input: Raw video stream or images.
Output: Annotated frames with bounding boxes and license plate numbers displayed.
## 🛠️ Contributing
Contributions are welcome! Please follow these steps:
Fork the repository.
Create your feature branch (git checkout -b feature-xyz).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-xyz).
Open a pull request.
## 📄 License
This project is licensed under the MIT License.

## 🙌 Acknowledgements
YOLOv8 - Ultralytics
EasyOCR
SORT Algorithm
## ⭐ Star this repository if you found it useful!
