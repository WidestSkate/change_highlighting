import cv2
import numpy as np
import time


def capture_grayscale_image():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default webcam

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    # Capture a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not capture frame.")
        cap.release()
        return None

    # Convert the captured frame to grayscale
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Release the webcam
    cap.release()

    return grayscale_frame

def highlight_changes(images):

    rgb_images = [None, None]

    rgb_images[0] = cv2.cvtColor(images[0], cv2.COLOR_GRAY2BGR)
    rgb_images[1] = cv2.cvtColor(images[1], cv2.COLOR_GRAY2BGR)

    
    for i in range(0, 480):
        for j in range(0, 640):
            if rgb_images[0][i][j][0] - rgb_images[1][i][j][0] > 100 or rgb_images[0][i][j][0] - rgb_images[1][i][j][0] < -100 :
                rgb_images[1][i][j] = [0,255,0]
    
    return rgb_images[1]
    


grayscale_images = [None, None]

# Call the function and get the grayscale image
grayscale_images[0] = capture_grayscale_image()
time.sleep(1)
grayscale_images[1] = capture_grayscale_image()



# Display the grayscale image (optional)
cv2.imshow("Image", highlight_changes(grayscale_images))
cv2.waitKey(0)
cv2.destroyAllWindows()
