from preprocessing import preprocess_image

image_path = "uploads/test.jpg"

try:
    result = preprocess_image(image_path)
    print("Preprocessing Successful")
    print("Output Shape:", result.shape)
except Exception as e:
    print("Error:", e)
