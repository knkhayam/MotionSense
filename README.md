# MotionSense

**MotionSense** is a lightweight, real-time motion detection system implemented in Python using OpenCV. It runs efficiently on edge devices with basic GPUs and robustly detects meaningful motion by filtering out noise and minor movements. The system overlays motion intensity as a heatmap on live camera feed and provides an alert trigger when motion exceeds a configurable threshold.

# Demo
![MotionSense Demo](motion_sense_output.gif)


# Testing
I used a generic public video available online on the internet to experimet this. 
placed in data/vid.mp4

---

## Features

- Real-time motion detection with live camera feed/or Video for example.
- Noise-resistant detection using optical flow and Gaussian smoothing.
- Motion intensity heatmap overlay for visual feedback.
- Configurable motion strength and minimum area thresholds.
- Trigger alert when motion covers a configurable percentage of the frame. such as in Crowd.
- Displays live FPS on the video.
- Lightweight and optimized for edge devices.

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/knkhayam/MotionSense.git
   cd MotionSense
2. Install dependencies
   ```bash
   pip install -r requirements.txt
3. Usage
   ```bash
   python motion_sense.py

## Configuration
You can adjust the following parameters inside motion_sense.py:

Parameter	Description	Default
MOTION_THRESHOLD	Minimum optical flow magnitude to consider motion valid	90
MIN_AREA	Minimum number of motion pixels to ignore noise/small motion	500
TRIGGER_PERCENT	Percentage of frame motion area to trigger alert	5
ALPHA	Weight for the original frame in overlay	0.6
BETA	Weight for the heatmap overlay	0.4


## License
MIT License © 2025


Feel free to reach out or open issues/pull requests!
