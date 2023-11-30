import cv2
import numpy as np


def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 75, 200)
    return edged


def find_card_contours(edged):
    contours, _ = cv2.findContours(
        edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def extract_number_roi(image, contour):
    x, y, w, h = cv2.boundingRect(contour)
    # Adjust these values as needed
    roi = image[y:y + h//4, x:x + w//4]
    return roi


def recognize_number(roi):
    # Placeholder for number recognition logic
    # For real use, apply machine learning or template matching here
    return "Number"


def process_image(image_path):
    image = cv2.imread(image_path)
    edged = preprocess_image(image)
    contours = find_card_contours(edged)

    for contour in contours:
        roi = extract_number_roi(image, contour)
        number = recognize_number(roi)
        print(f"Detected Number: {number}")
        cv2.imshow("ROI", roi)
        cv2.waitKey(0)

    cv2.destroyAllWindows()


# Replace with your image path
# process_image("data/playing_cards.jpg")
process_image("data/playing-cards-hearts-suit.webp")
