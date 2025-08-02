import cv2
from ultralytics import YOLO

# Load your trained model
model = YOLO("best.pt")

# Video source: file or webcam
video_path = "99385-653120176_tiny.mp4"  # or use 0 for webcam
cap = cv2.VideoCapture(video_path)

# Define the output video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec
out = cv2.VideoWriter("oil_spill_output.mp4", fourcc, 30.0,
                      (int(cap.get(3)), int(cap.get(4))))

# Loop through video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run prediction on current frame
    results = model.predict(source=frame, conf=0.3, verbose=False)

    # Draw results on frame
    annotated_frame = results[0].plot()

    # Write to output file
    out.write(annotated_frame)

    # Show frame live
    cv2.imshow("Oil Spill Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
