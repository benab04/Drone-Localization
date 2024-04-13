import cv2
from ultralytics import YOLO

# Load the YOLOv5 model
model = YOLO("runs/detect/train2/weights/200_epoch.pt")

# Configuration for the detection task
config = {
    "path": "/drone_dataset",
    "train": "/drone_dataset/train",
    "val": "/drone_dataset/valid",
    "nc": 1,  # Number of classes
    "names": ["drone"],  # Class names
}

# Open the video file
video_path = "path/to/your/video.mp4"
video_capture = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video_capture.get(cv2.CAP_PROP_FPS))
codec = cv2.VideoWriter_fourcc(*'XVID')

# Define the output video writer
output_video_path = "output_video_with_boxes.avi"
output_video = cv2.VideoWriter(output_video_path, codec, fps, (frame_width, frame_height))

# Process each frame of the video
while video_capture.isOpened():
    ret, frame = video_capture.read()

    if not ret:
        break

    # Detect objects in the frame
    results = model(frame)

    # Draw bounding boxes and confidence scores
    if results.pred:
        for result in results.pred:
            for det in result:
                box = det.xyxy[0].cpu().numpy()
                conf = det.conf.item()
                if conf > 0.30:
                    start = (int(box[0]), int(box[1]))
                    end = (int(box[2]), int(box[3]))
                    frame = cv2.rectangle(frame, start, end, (0, 255, 0), 2)
                    frame = cv2.putText(frame, f'conf: {conf:.3f}', start, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

    # Write the frame to the output video
    output_video.write(frame)

# Release video capture and writer
video_capture.release()
output_video.release()

# Close all windows
cv2.destroyAllWindows()

print("Video processing completed. Output video saved at:", output_video_path)
