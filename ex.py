
import os, random, shutil

# Paths
base = r"C:/Users/prana/OneDrive/Desktop/yolov8_train"
images_dir = os.path.join(base, "images/train")
labels_dir = os.path.join(base, "labels/train")

val_images_dir = os.path.join(base, "images/val")
val_labels_dir = os.path.join(base, "labels/val")

# Create val folders
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# Get all images
images = [f for f in os.listdir(images_dir) if f.endswith((".jpg", ".png"))]

# Pick 20% for validation
val_count = int(len(images) * 0.2)
val_images = random.sample(images, val_count)

# Move files
for img in val_images:
    # Move image
    shutil.move(os.path.join(images_dir, img), os.path.join(val_images_dir, img))
    # Move label
    label = img.rsplit(".", 1)[0] + ".txt"
    if os.path.exists(os.path.join(labels_dir, label)):
        shutil.move(os.path.join(labels_dir, label), os.path.join(val_labels_dir, label))
