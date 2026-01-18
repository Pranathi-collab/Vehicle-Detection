import os
import cv2
from ultralytics import YOLO

# -----------------------------
# 1. Load your trained YOLO model
# -----------------------------
# Replace with the actual path to your weights file
model_path = r"C:\Python\training_data\project\models\license_detector.pt"
model = YOLO(model_path)

# -----------------------------
# 2. Path to the test image
# -----------------------------
image_path = "C:/Python/training_data/project/test_image.py.png"
results = model.predict(
    source=image_path,  
    conf=0.25,           
    save=True,          
    show=True            
)
