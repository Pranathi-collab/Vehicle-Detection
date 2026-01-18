import os
import cv2
import numpy as np
from ultralytics import YOLO

# Path to your image
image_path = r"C:\Python\training_data\auto.webp"
image_out_path = f"{image_path}_out.jpg"

# Load YOLO model
model_path = "C:/Python/training_data/project/models/license_detector.pt"
model = YOLO(model_path)

# Read image
image = cv2.imread(image_path)
if image is None:
    raise RuntimeError("Error: Could not read the image.")

H, W, _ = image.shape

# Run YOLO inference
results = model(image)

threshold = 0.25

# Draw detections
for r in results:
    for box in r.boxes:
        if box.conf[0] >= threshold:
            x1, y1, x2, y2 = box.xyxy[0].int().tolist()
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = f"{model.names[cls]} {conf:.2f}"
            cv2.rectangle(image, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(image, label, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

# Save output image
cv2.imwrite(image_out_path, image)

# Optionally display
cv2.imshow("Detections", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
