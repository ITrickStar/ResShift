import sys
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def compare_images(imageA_path, imageB_path):
    imageA = cv2.imread(imageA_path)
    imageB = cv2.imread(imageB_path)
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    m = mse(grayA, grayB)
    s = ssim(grayA, grayB)
    return m, s


def get_image_resolution(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Не удалось загрузить изображение.")
        return None
    return (image.shape[1], image.shape[0])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: python script.py <path>")
        sys.exit(1)

    image_path = sys.argv[1]

    resolution = get_image_resolution(image_path)
    if resolution:
        print("Разрешение изображения:", resolution)
