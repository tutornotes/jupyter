import kagglehub
import os
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# a) Load dataset
path = kagglehub.dataset_download("aruchomu/data-for-yolo-v3-kernel")
print("Dataset path:", path)

weights_path = os.path.join(path, "yolov3.weights")
names_path = os.path.join(path, "coco.names")

# FIX: Download cfg if missing
if not os.path.exists("yolov3.cfg"):
    import urllib.request
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg",
        "yolov3.cfg"
    )

config_path = "yolov3.cfg"

# Load class labels
with open(names_path, "r") as f:
    classes = f.read().splitlines()

# b) Load YOLOv3 model
net = cv2.dnn.readNet(weights_path, config_path)

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# c) Open video source
video_path = os.path.join(path, "detections.gif")
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape

    # d) Forward pass
    blob = cv2.dnn.blobFromImage(
        frame, 1/255.0, (416, 416), swapRB=True, crop=False
    )

    net.setInput(blob)
    outputs = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply NMS
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # e) Draw bounding boxes
    if len(indexes) > 0:
        for i in indexes:
            i = i[0] if isinstance(i, (list, tuple, np.ndarray)) else i
            x, y, w, h = boxes[i]

            label = classes[class_ids[i]]
            conf = confidences[i]

            text = f"{label} {conf:.2f}"

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(
                frame,
                text,
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,255,0),
                2
            )

    cv2_imshow(frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()