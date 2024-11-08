from ultralytics import YOLO
import cv2
import torch
import numpy as np
from torchvision import transforms
import pandas as pd

# Load MiDaS depth estimation model
midas = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
midas.eval()

# Define the input transformation for MiDaS
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((384, 384)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])

# {1:[[w],[l],[d]]}

df = pd.DataFrame({'ID': [], 'Width': [], 'Height': [], 'Depth': []})

l1,l2,l3,l4 = [],[],[],[]
def add_data (ids , width ,height ,depth):
    l1.append(ids[0])

# new_df = pd.DataFrame({'ID': [], 'Width': [], 'Height': [], 'Depth': []})
def excute_data ():
    data = {
        'Id': l1,
        'Height': l2,
        'width': l3,
        'depth': l4
    }
    df1 = pd.DataFrame(data)
    df_mean = df1.groupby('Id').mean().reset_index()
    df_mean.to_csv('df_mean.csv', index=False)
    print (df_mean)

def estimate_depth(frame, box):
    x1, y1, x2, y2 = box
    crop = frame[y1:y2, x1:x2]
    input_batch = transform(crop).unsqueeze(0)

    with torch.no_grad():
        depth = midas(input_batch).squeeze().cpu().numpy()

    # Calculate the median depth instead of the average
    median_depth = np.median(depth)

    # Convert depth from meters to centimeters
    median_depth_cm = median_depth / 100
    return median_depth_cm


# Load the YOLO model for pothole detection
model = YOLO(r'C:\Users\moham\PycharmProjects\Potholes_Detection\best2.pt')

# Open the video capture
cap = cv2.VideoCapture(
    r'C:\Users\moham\PycharmProjects\Potholes_Detection\vid1.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detect potholes
    results = model.track(frame, persist=True, conf=0.7)
    detections = results[0].boxes

    for detection in detections:
        box = detection.xyxy[0]
        conf = detection.conf[0]
        cls = detection.cls[0]
        ids = detection.id[0] if detection.id is not None else -1
        x1, y1, x2, y2 = map(int, box[:4])

        width = x2 - x1
        height = y2 - y1

        # Use median depth in centimeters
        depth_map = estimate_depth(frame, (x1, y1, x2, y2))
        depth_text = f"Pothole{ids} - Width: {width}, Height: {height}, Depth: {depth_map:.2f} cm"

        if width*height >= 23000 or depth_map >= 2.0 :
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, depth_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        else:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, depth_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        l1.append(int(ids))
        l2.append(height)
        l3.append(width)
        l4.append(depth_map)


        # Display the information
        print(f"Pothole{ids} - Width: {width}, Height: {height}, Depth: {depth_map:.2f} cm")

    # annotated_frame = results[0].plot()
    cv2.imshow("Pothole", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

excute_data()
cap.release()
cv2.destroyAllWindows()
print('Done')