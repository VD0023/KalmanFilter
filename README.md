## Project Documentation: Kalman Filter Color Detection

### Introduction
The Kalman Filter Color Detection project aims to implement a Kalman filter using Python and OpenCV to detect and track a specific color in a video stream. The Kalman filter is a powerful mathematical algorithm widely used for state estimation in various fields, including control systems, robotics, and signal processing. In this project, the Kalman filter is employed to estimate the position of a colored object in real-time, even in the presence of noise and uncertainties.

### Dependencies
To run this project, you need the following dependencies:

- Python 3.x
- OpenCV (cv2) library
- NumPy library
- JSON library

### Implementation
The project consists of a Python script, "kalman_filter_color_detection.py," which performs the following steps:

1. Importing Libraries:
   The necessary libraries, including cv2, numpy, and json, are imported to provide the required functionalities for video processing, numerical operations, and JSON file handling.

2. Kalman Filter Initialization:
   The Kalman filter is initialized using the `cv2.KalmanFilter` class. The filter is configured with a state dimension of 4 and a measurement dimension of 2. The measurement and transition matrices are defined to establish the relationship between the state variables and the measurements. Additionally, the process noise covariance is set to account for the uncertainty in the system dynamics.

3. Video Capture:
   The script initializes the video capture from the default camera (index 0). It continuously reads frames from the video stream.

4. Color Detection:
   Each frame is processed to detect a specific color using color segmentation in the HSV color space. The target color range is defined by lower and upper threshold values. The script uses the `cv2.inRange` function to create a binary mask indicating the presence of the color in the frame.

5. Contour Extraction:
   The largest contour within the color mask is extracted using the `cv2.findContours` function. The contour represents the object's shape corresponding to the detected color.

6. Position Estimation:
   The script computes the centroid (x, y) coordinates of the largest contour using the moments method provided by OpenCV. These coordinates serve as the measured position of the object.

7. Kalman Filter Prediction and Correction:
   The Kalman filter's `predict` method is called to estimate the next state of the system based on the previous state and the transition matrix. Then, the measured position is fed into the filter using the `correct` method to update the estimated state based on the measurement. The filter provides the predicted position of the object.

8. Data Collection:
   The script collects relevant information, including the frame, detected color, predicted position, and measured position, in a dictionary format. This information is appended to a list for further analysis or storage.

9. Visualization:
   The processed frame, including the color detection and tracked object, is displayed using the `cv2.imshow` function.

10. Program Termination:
    Pressing the 'q' key terminates the program execution.

11. Data Storage:
    Upon termination, the collected information is saved in a JSON file named "collected_info.json" using the `json.dump` function.

### Usage
To use the Kalman Filter Color Detection project, follow these steps:

1. Install the required dependencies: Python, OpenCV, NumPy, and JSON libraries.

2. Download the "kalman_filter_color_detection.py" script.

3. Execute the script using a Python interpreter or IDE.

4. The script will access the default camera and display the video stream with color detection and tracking.

5. Press the '

q' key to terminate the program. The collected information will be stored in the "collected_info.json" file.

### Customization
To customize the project for different color detection scenarios, you can modify the following parameters:

- Lower and upper color threshold values: Adjust the HSV color range values (`lower_color` and `upper_color`) to target different colors in the video stream.

- Kalman filter parameters: Modify the matrices in the Kalman filter initialization section (`measurementMatrix`, `transitionMatrix`, `processNoiseCov`) to adapt to the specific system dynamics and measurement characteristics.

### Conclusion
The Kalman Filter Color Detection project provides an implementation of a Kalman filter for real-time color detection and tracking. By leveraging the power of the Kalman filter algorithm, the project allows accurate estimation of the position of a colored object in the presence of noise and uncertainties. This project can serve as a foundation for various applications requiring robust object tracking, such as robotics, computer vision, and automation systems.

### Acknowledgments
This project was developed by Vansh Dahiya as a demonstration of the Kalman filter's capabilities in color detection and tracking. It builds upon the OpenCV and NumPy libraries, which provide essential tools for computer vision and numerical operations, respectively. Special thanks to Rudolf Kalman for his pioneering work on the Kalman filter algorithm.

For any inquiries or suggestions, please contact Vanshdahiya00@gmail.com

