import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
image_path = "group.jpeg"
image = cv2.imread(image_path)

result = model(image)
count = 0
for r in result:
    for box in r.boxes:
        cls = int(box.cls[0])  # Accessing the first element directly
        label = model.names[cls]
        conf = float(box.conf[0])

        if label == "person" and conf > 0.5:
            count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Accessing the coordinates directly
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2),

            # Fixing the string formatting in the label and confidence text
            cv2.putText(image, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Fixing the string formatting for the people count
            cv2.putText(image, f"People Count: {count}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()