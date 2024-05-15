import sys
import cv2

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
