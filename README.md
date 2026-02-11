# Cell Phone Detection System

A real-time cell phone detection system using YOLOv8 and OpenCV that alerts you when a cell phone is detected via webcam.

## Features

- Real-time cell phone detection using YOLOv8
- Audio alert when phone is detected
- Visual alert popup with custom image
- Bounding box and confidence score display
- Optimized for speed with frame skipping

## Requirements

- Python 3.8+
- Webcam

## Installation

1. Clone or download this project

2. Install required packages:
```bash
pip install opencv-python ultralytics pygame
```

3. Add your files:
   - `Get Out.mp3` - Audio alert file (place in project folder)
   - `picture.jpg` - Alert image (place in project folder)

## Usage

Run the script:
```bash
python test_camera.py
```

**Controls:**
- Press `q` to quit

## How It Works

1. Captures video from webcam (camera index 1)
2. Runs YOLOv8 detection every 2 frames for speed
3. When cell phone detected with >50% confidence:
   - Draws green bounding box
   - Plays audio alert
   - Shows alert image for 0.5 seconds

## Configuration

You can adjust these settings in the code:
```python
cap = cv2.VideoCapture(1)  # Change camera index (0, 1, 2...)
model = YOLO("yolov8s.pt")  # Change model (yolov8n.pt, yolov8m.pt, etc.)
frame_count % 2  # Change to 3 or 4 for even faster processing
confidence > 0.5  # Adjust detection threshold (0.0 to 1.0)
```

## Troubleshooting

**Slow performance:**
- Use smaller model: `yolov8n.pt`
- Increase frame skip: `frame_count % 3`
- Lower camera resolution

**Camera not found:**
- Change camera index from 1 to 0 or 2

**Audio not playing:**
- Make sure `Get Out.mp3` is in the same folder
- Check file name spelling

## License

Free to use and modify.
