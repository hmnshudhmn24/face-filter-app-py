import cv2
import numpy as np

# Load the face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the filter (example: sunglasses)
filter_img = cv2.imread('sunglasses.png', cv2.IMREAD_UNCHANGED)

def apply_filter(frame, face_x, face_y, face_w, face_h):
    """Apply a filter over the detected face."""
    filter_resized = cv2.resize(filter_img, (face_w, int(face_h / 2)))

    for c in range(0, 3):
        frame[face_y:face_y + filter_resized.shape[0], face_x:face_x + filter_resized.shape[1], c] =             frame[face_y:face_y + filter_resized.shape[0], face_x:face_x + filter_resized.shape[1], c] *             (1 - filter_resized[:, :, 3] / 255.0) + filter_resized[:, :, c] * (filter_resized[:, :, 3] / 255.0)

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            apply_filter(frame, x, y, w, h)

        cv2.imshow('Face Filter App', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
