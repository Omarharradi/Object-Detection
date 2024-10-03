import cv2
import torch

# Load the YOLOv5 model (small version)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s.pt')  # Adjust the path if needed

# Initialize camera
cap = cv2.VideoCapture(0)  # Use the correct camera index

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Perform inference
    results = model(frame)

    # Process results
    frame = results.render()[0]  # Render the results on the frame

    # Display the resulting frame
    cv2.imshow('YOLOv5 Object Detection', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
