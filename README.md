<<<<<<< HEAD
# License Plate Detection using YOLOv8

A computer vision project for detecting license plates in images and videos using YOLOv8 (You Only Look Once) deep learning model.

## 📋 Overview

This project implements an object detection system specifically trained to detect license plates in various scenarios. It uses the Ultralytics YOLOv8 framework for training and inference. The dataset was annotated using CVAT (Computer Vision Annotation Tool), a web-based annotation platform.

## 🗂️ Project Structure

```
training_data/
├── project/
│   ├── main.py              # Training script for YOLOv8 model
│   ├── pred.py              # Prediction script for images
│   ├── img.py               # Image processing utilities
│   └── models/
│       └── license_detector.pt    # Trained model weights
├── runs/
│   └── detect/              # Training results and outputs
│       ├── train/           # Training run 1
│       ├── train2/          # Training run 2
│       └── ...
├── videos/                  # Input/output videos
├── ex.py                    # Dataset preparation utilities
├── yolov8n.pt              # Pre-trained YOLOv8 nano weights
└── venv/                   # Virtual environment
```

## 🚀 Features

- **License Plate Detection**: Detect license plates in images and videos
- **Custom Training**: Train YOLOv8 on custom license plate dataset
- **Multiple Training Runs**: Experiment tracking with different training configurations
- **Image & Video Processing**: Support for both static images and video streams
- **Model Inference**: Pre-trained model for quick predictions

## 📦 Dependencies

The project requires Python 3.x with the following packages:

- `ultralytics` - YOLOv8 framework
- `opencv-python` (cv2) - Image/video processing
- `numpy` - Numerical operations
- `torch` - PyTorch deep learning framework
- `torchvision` - Computer vision utilities

## 🛠️ Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd C:\Python\training_data
   ```

2. **Activate the virtual environment:**
   ```bash
   venv\Scripts\activate
   ```

3. **Install dependencies (if not already installed):**
   ```bash
   pip install ultralytics opencv-python numpy torch torchvision
   ```

## 📖 Usage

### Training the Model

To train the YOLOv8 model on your custom dataset:

```python
python project/main.py
```

Make sure to update the `data` path in `main.py` to point to your dataset configuration file.

### Making Predictions

#### On Images

Use `pred.py` or `img.py` for image inference:

```python
python project/pred.py
```

Update the `image_path` and `model_path` variables in the script to match your file locations.

#### Configuration Options

- `conf`: Confidence threshold (default: 0.25)
- `save`: Save output image (default: True)
- `show`: Display results (default: True)

### Dataset Preparation

The dataset was annotated using **CVAT (Computer Vision Annotation Tool)**, a web-based platform for annotating images and videos for computer vision tasks. After annotation, the dataset was exported in YOLO format for training.

Use `ex.py` for dataset preparation tasks such as train/validation split:

```python
python ex.py
```

## 🎯 Model Details

- **Base Model**: YOLOv8n (nano version)
- **Task**: Object Detection
- **Classes**: License plates
- **Input Format**: Images (JPG, PNG, WEBP) and Videos (MP4)
- **Output Format**: Bounding boxes with confidence scores

## 📊 Training Results

Training runs are saved in the `runs/detect/` directory. Each run includes:

- Model weights (`best.pt`, `last.pt`)
- Training curves and metrics
- Confusion matrices
- Validation results
- Configuration files (`args.yaml`)

Latest trained model is available at: `project/models/license_detector.pt`

## 📝 Notes

- The dataset was sourced from **GitHub** and annotated using **CVAT (Computer Vision Annotation Tool)** - a web-based annotation platform
- The model is trained on a custom annotated dataset for license plate detection
- Multiple training runs (train through train9) were conducted for experimentation
- Best model weights are copied to `project/models/license_detector.pt` for easy access
- Input images are processed and saved with `_out.jpg` suffix

## 📦 Dataset Information

- **Dataset Source**: The dataset was obtained from GitHub
- **Annotation Tool**: CVAT (Computer Vision Annotation Tool) - https://cvat.org
- **Dataset Format**: YOLO format (bounding box annotations in `.txt` files)
- **Annotation Type**: Bounding boxes for license plates
- **Workflow**: The dataset was downloaded from GitHub, annotated using CVAT, and then exported in YOLO format for training

## 🔧 Configuration

Training parameters can be modified in `project/main.py`:
- Number of epochs
- Dataset path
- Model size (nano, small, medium, large, xlarge)

## 📄 License

This project is for educational and research purposes.

## 👤 Author

Pranathi2004

---

**Note**: Make sure to update file paths in the scripts according to your system configuration before running.
