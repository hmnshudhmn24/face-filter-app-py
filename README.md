# Face Filter App

## Overview
A **fun face filter application** that detects faces in real-time using OpenCV and applies cool filters like sunglasses, hats, or masks.

## Features
- **Real-time face detection** using OpenCV Haar cascades.
- **Applies fun filters** like sunglasses over the face.
- **Works with webcam input.**

## Requirements
Install dependencies using:
```
pip install opencv-python numpy
```

## Usage
1. Place your filter image (e.g., `sunglasses.png`) in the same directory.
2. Run the script:
```
python face_filter_app.py
```
3. Press `q` to exit.

## Notes
- You can replace `sunglasses.png` with any transparent PNG filter.
- Modify `apply_filter()` to position filters accurately.
