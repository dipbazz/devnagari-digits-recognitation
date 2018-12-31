import numpy as np
import cv2
import os
from .digit_recognizer import recognize_digit


def readImage(image_name):
    image_path = "media/"+ str(image_name)
    img = cv2.imread(image_path)
    copy_img = img[:, :]

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    dilated = cv2.dilate(thresh, kernel, iterations=1)
    erod = cv2.erode(dilated, kernel, iterations=7)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

    dilated = cv2.dilate(erod, kernel, iterations=2)

    _, thresh = cv2.threshold(dilated, 127, 255, cv2.THRESH_BINARY_INV)

    _, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    predicted_digit = []
    for contour in contours:
        [x, y, w, h] = cv2.boundingRect(contour)

        # resizing the dilated images for 32x32 size of image
        resize_img = cv2.resize(thresh[y - 2:y + h + 2, x - 2:x + w + 2], (32, 32))

        predicted_img = recognize_digit(np.array([resize_img.reshape(1024,)]))

        cv2.rectangle(copy_img, (x-2, y-2), (x+w+2, y+h+2), (0, 0, 255), 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(copy_img, str(predicted_img), (x+10, y-10), font, 0.7, (0,0,255), 1, cv2.LINE_AA)
        predicted_digit.append(predicted_img)
        

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_dir = os.path.join(BASE_DIR, 'Home\static\Home\images')
    cv2.imwrite(img_dir + '\output.jpg', copy_img)

    return True

