import cv2
from ultralytics import YOLO

model = YOLO("helmet.pt")
image_path = "helmetgroup.jpg"
image = cv2.imread(image_path)

result = model(image)
print(result)

object_count = {}
for r in result:
    for box in r.boxes:
        cls = int(box.cls[0])
        label = model.names[cls]
        conf = float(box.conf[0])

        if conf > 0.5:
            object_count[label] = object_count.get(label, 0) + 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2),


            cv2.putText(image, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            y_offset = 30
            for label in object_count.items():

                cv2.putText(image, "{label} : {count}", (20, y_offset),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            y_offset += 30

            cv2.imshow("Bottles", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()