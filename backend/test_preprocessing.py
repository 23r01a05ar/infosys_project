from preprocessing import preprocess_image
import cv2
import os

UPLOAD_FOLDER = "uploads"


if not os.path.exists(UPLOAD_FOLDER):
    print("Uploads folder not found")
    exit()


files = [os.path.join(UPLOAD_FOLDER, f) for f in os.listdir(UPLOAD_FOLDER)]

if not files:
    print("No images found in uploads folder")
    exit()

latest_file = max(files, key=os.path.getctime)

print("\nUsing File:", latest_file)

# ---------- BEFORE PREPROCESSING ----------
original = cv2.imread(latest_file)

if original is None:
    print("Error loading image")
    exit()

original_rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

print("\n========== BEFORE PREPROCESSING ==========")
print("Original Shape (Height, Width, Channels):", original_rgb.shape)
print("Original Pixel Range:", original_rgb.min(), "to", original_rgb.max())
print("Sample Pixel Value:", original_rgb[0][0])

# ---------- AFTER PREPROCESSING ----------
processed = preprocess_image(latest_file)

print("\n========== AFTER PREPROCESSING ==========")
print("Processed Shape (Height, Width, Channels):", processed.shape)
print("Processed Pixel Range:", processed.min(), "to", processed.max())
print("Sample Pixel Value:", processed[0][0])

print("\n✅ Preprocessing Successful")
