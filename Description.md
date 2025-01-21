Automatic Number Plate Recognition (ANPR) Using Python and YOLOv8

#Overview
The Automatic Number Plate Recognition (ANPR) system is a computer vision project that detects and recognizes vehicle license plates using the YOLOv8 object detection model and EasyOCR for text recognition. This project can be used in traffic monitoring, toll systems, and parking management systems.

This document serves as a guide to create the repository for your project, including a detailed description, file structure, and usage instructions.


Features
- Vehicle Detection: Identifies vehicles in a video stream or image.
- License Plate Detection: Locates license plates using a YOLOv8-trained model.
- Text Recognition: Extracts the license plate characters using EasyOCR.
- Tracking: Tracks vehicles using the SORT algorithm.
- Real-time Analysis: Processes video streams in real time.


Requirements
To run this project, you need the following:

1. Software
   - Python 3.8 or later
   - pip (Python package manager)

2. Python Libraries
   - ultralytics
   - easyocr
   - opencv-python
   - numpy
   - matplotlib
   - sort (download from the SORT repository)

3. Hardware
   - A GPU-enabled system for faster inference (optional but recommended).

4. Dataset
   - A labeled dataset of vehicle images and license plates for training and testing YOLOv8.



File Structure

automatic-number-plate-recognition-python-yolov8/
|-- README.md
|-- LICENSE
|-- requirements.txt
|-- main.py
|-- util.py
|-- visualize.py
|-- add_missing_data.py
|-- models/
|   |-- yolov8_trained_model.pt
|-- data/
|   |-- video.mp4
|   |-- images/
|       |-- example_image.jpg




 Installation
1. Clone the repository:
   bash
   git clone https://github.com/yourusername/automatic-number-plate-recognition-python-yolov8.git
   cd automatic-number-plate-recognition-python-yolov8
   

2. Install dependencies:
   bash
   pip install -r requirements.txt
   

3. Download the SORT module:
   - Follow the instructions in [SORT Repository](https://github.com/abewley/sort) to install the module.

4. Add the trained YOLOv8 model to the models/ directory.



How It Works
1. Vehicle Detection:
   - The pretrained YOLOv8 model detects vehicles in the given video or image.

2. License Plate Detection:
   - A custom-trained YOLOv8 model detects license plates.

3. Text Recognition:
   - EasyOCR extracts text from the detected license plate regions.

4. Visualization:
   - Bounding boxes and recognized text are displayed on the processed frames.



Usage
1. Run the main.py file to process a video or image file:
   bash
   python main.py --input data/video.mp4
   
   
   Options:
   - --input: Path to the input video or image file.
   - --output: Path to save the processed video (optional).

2. To visualize intermediate results, use:
   bash
   python visualize.py
   

