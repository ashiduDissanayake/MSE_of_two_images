import cv2
import numpy as np

def compute_mse(image1_path, image2_path):
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    if img1 is None or img2 is None:
        raise ValueError("Path Error")

    if img1.shape != img2.shape:
        raise ValueError("Image Dimension Error")

    mse = np.mean((img1.astype("float") - img2.astype("float")) ** 2)
    return mse


# Example usage:
img1_path = "./raw.jpg"
img2_path = "./notraw.jpeg"
mse_value = compute_mse(img1_path, img2_path)
print(f"Mean Squared Error: {mse_value}")
