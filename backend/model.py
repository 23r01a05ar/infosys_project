import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions

# Load pretrained model
model = MobileNetV2(weights="imagenet")

def predict_product(image_array):

    image_batch = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_batch)
    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]

    results = []

    for _, label, confidence in decoded:
        results.append({
            "product": label,
            "confidence": float(confidence),
            "keywords": label.replace("_", " ").split()
        })

    return results

