from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2

# Load the trained model
model = YOLO("best.pt")  # make sure best.pt is in your current working directory

# Path to the image you want to test
image_path = "img.jpg"  # replace with your image file name

# Run prediction
results = model.predict(source=image_path, save=True, conf=0.3)  # conf=0.3 is confidence threshold

# Show the image with bounding boxes
# Result image is saved to 'runs/detect/predict' by default
predicted_img_path = "runs/detect/predict/test.jpg"  # same name as input image

# Load and display the predicted image
img = cv2.imread(predicted_img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 8))
plt.imshow(img_rgb)
plt.axis('off')
plt.title("Predicted Output")
plt.show()
