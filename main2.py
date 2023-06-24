#Azul23
import cv2
import numpy as np
import json


def kalman_filter_color_detection():
#KalmanFiltrParameters
    kalman = cv2.KalmanFilter(4, 2)
    kalman.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
    kalman.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
    kalman.processNoiseCov = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32) * 0.03

    video_capture = cv2.VideoCapture(0)
    collected_info = []

    while True:
#read frams
        ret, frame = video_capture.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_color = np.array([40, 50, 50])
        upper_color = np.array([80, 255, 255])
        mask = cv2.inRange(hsv_frame, lower_color, upper_color)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            largest_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest_contour)

            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                prediction = kalman.predict()
                measurement = np.array([[np.float32(cx)], [np.float32(cy)]])
                kalman.correct(measurement)

                info = {
                    'frame': frame.tolist(),
                    'color_detected': 'green',
                    'predicted_position': prediction.tolist(),
                    'measured_position': measurement.tolist()
                }
                collected_info.append(info)
        cv2.imshow('Kalman Filter Color Detection', frame)

#q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break