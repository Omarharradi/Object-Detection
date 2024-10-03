![Demo of YOLOv5 in Action](video.gif)




# **YOLOv5 Object Detection with OpenCV and iPhone Webcam**


This project utilizes the YOLOv5 model for real-time object detection integrated with OpenCV. The script captures live video from an iPhone used as a webcam, processes each frame to detect objects, and displays bounding boxes and labels on the video stream.

## **Features**
- Real-time object detection using the YOLOv5 model.
- Detection and labeling of multiple objects in the live video feed.
- Utilizes OpenCV for video capture and frame rendering.
- iPhone is configured to act as a webcam.

## **About YOLOv5**
YOLOv5 (You Only Look Once version 5) is an advanced, state-of-the-art object detection model developed by Ultralytics. It is designed for speed and accuracy, making it suitable for real-time applications. YOLOv5 operates by dividing the input image into a grid and predicting bounding boxes and class probabilities for each grid cell. This model is popular for its high performance and ease of use.

### **Version Used**
This project specifically uses the YOLOv5 small version (`yolov5s.pt`), which is optimized for speed and smaller model size, making it an excellent choice for real-time detection tasks on devices with limited computational resources.

## **Camera Setup**
The project is set up to use an iPhone as a webcam. The camera index for the iPhone is set to `0`. This means that the script will capture video from the first camera detected by the system, which is typically the iPhone when connected through applications like **EpocCam** or **Camo**.

## **Installation**

### **1. Python Version**
Ensure you have **Python 3.8** or higher installed on your machine.

### **2. Required Libraries**
Install the necessary Python packages using `pip`:
- **PyTorch**: for loading the YOLOv5 model.
- **OpenCV**: for video capture and rendering.

### **3. Model File**
Download the YOLOv5 model weights (`yolov5s.pt`) from the official YOLOv5 GitHub repository or allow the script to download it automatically.

## **Usage**
To run the project, execute the provided Python script. Ensure that your iPhone is connected as a webcam and that the correct camera index is set.

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
