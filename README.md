# Advanced Face Recognition System.

## Project Overview

This project is an advanced face recognition system developed to recognize faces in real-time using a webcam. It integrates various techniques to enhance the accuracy and efficiency of face recognition, even from a distance of up to 0.8 meters. The system is implemented using Python, OpenCV, face_recognition, and NumPy.

## Features

- **Real-time Face Recognition:** Detects and recognizes faces in real-time using a webcam.
- **Distance Recognition:** Optimized to recognize faces from a distance of up to 0.8 meters.
- **Efficient Processing:** Reduced lag through frame resizing and optimized face detection.
- **Enhanced Visuals:** Improved text styling for better visual presentation.
- **User-friendly Interface:** Clean and intuitive interface for easy use.
- **Well-organized Code:** Clear comments and structure for better readability and maintenance.

## Technical Details

### Libraries Used

- **OpenCV:** For image and video processing.
- **face_recognition:** For face detection and recognition.
- **NumPy:** For numerical operations.

### How It Works

1. **Face Encoding:** 
    - Loads images from a specified folder.
    - Encodes faces from the images using the `face_recognition` library.
    
2. **Real-time Detection:**
    - Captures video frames from the webcam.
    - Resizes frames for faster processing.
    - Detects faces in the resized frames and matches them against the encoded faces.
    
3. **Visual Feedback:**
    - Draws rectangles around detected faces.
    - Displays the name of the recognized person above the rectangle.

### Challenges Faced

- **Lag Reduction:** Optimized frame resizing to significantly reduce lag.
- **Distance Recognition:** Tuned the model to recognize faces accurately from a greater distance.
- **Visual Enhancement:** Improved text styling for better readability.

## Getting Started

### Prerequisites

- Python 3.x
- OpenCV
- face_recognition
- NumPy

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/PR-ODINSON/Face_recognition_model.git
    cd Face_recognition_model
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. Place your images in the `images` folder for face encoding.

### Running the Project

Run the main script:
```sh
python main.py
