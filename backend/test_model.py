from preprocessing import preprocess_image
from model import predict_product
import os

TEST_FOLDER = "../product_test_images"

images = os.listdir(TEST_FOLDER)

total = 0
successful_predictions = 0

for img_name in images:
    img_path = os.path.join(TEST_FOLDER, img_name)

    try:
        processed = preprocess_image(img_path)
        result = predict_product(processed)

        print("\nImage:", img_name)
        print("Prediction:", result[0]["product"])
        print("Confidence:", result[0]["confidence"])

        total += 1

        # Consider prediction successful if confidence > 0.30
        if result[0]["confidence"] > 0.30:
            successful_predictions += 1

    except Exception as e:
        print("Error processing", img_name, e)

accuracy = (successful_predictions / total) * 100

print("\n======================")
print("Total Images Tested:", total)
print("Successful Predictions:", successful_predictions)
print("Model Accuracy:", round(accuracy, 2), "%")
