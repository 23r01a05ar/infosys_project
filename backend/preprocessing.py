import cv2
import numpy as np
from PIL import Image

STANDARD_SIZE = (224, 224)


def convert_to_rgb(image_path):
    image = Image.open(image_path).convert("RGB")
    return np.array(image)


def resize_image(image):
    return cv2.resize(image, STANDARD_SIZE)


def reduce_noise(image):
    return cv2.GaussianBlur(image, (5, 5), 0)


def normalize_image(image):
    return image / 255.0


def enhance_image(image):
    alpha = 1.2
    beta = 20
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)


def preprocess_image(image_path):
    image = convert_to_rgb(image_path)
    image = resize_image(image)
    image = reduce_noise(image)
    image = enhance_image(image)
    image = normalize_image(image)

    return image
