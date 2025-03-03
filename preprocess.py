import cv2

def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred

# Example usage
image = preprocess_image("test_images/sample.jpg")
cv2.imshow("Processed Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
