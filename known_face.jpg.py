import cv2

def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to open webcam.")
        return
    ret, frame = cap.read()
    cap.release()
    if not ret:
        print("Error: Unable to capture frame.")
        return
    cv2.imwrite('known_face.jpg', frame)

    print("Reference image saved as 'known_face.jpg'.")
capture_image()
