import cv2
from ultralytics import YOLO
import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound("Get Out.mp3")


picture = cv2.imread("picture.jpg")
cap = cv2.VideoCapture(1)
model = YOLO("yolov8s.pt")
frame_count = 0

while True:
    success, img = cap.read()
    if not success:
        break
    frame_count += 1
    if frame_count % 2 == 0:
        results = model(img, verbose=False)

        for result in results[0].boxes:
            cls_id = int(result.cls[0])
            confidence = float(result.conf[0])
            class_name = model.names[cls_id]

            if class_name == "cell phone" and confidence > 0.5:
                x1, y1, x2, y2 = map(int, result.xyxy[0])
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, f"{class_name} {confidence:.2f}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
                sound.play()
                cv2.imshow("Alert!", picture)
                cv2.waitKey(2000)
                cv2.destroyWindow("Alert!")

    cv2.imshow("Camera", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
