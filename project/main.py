from ultralytics import YOLO

# Load pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Train on your dataset
results = model.train(
    data="C:/Users/prana/OneDrive/Desktop/yolov8_train/config.yaml",
    epochs=50
)
