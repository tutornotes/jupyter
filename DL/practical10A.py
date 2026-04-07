import kagglehub
import os
import cv2
import numpy as np
from google.colab.patches import cv2_imshow 


path = kagglehub.dataset_download("aruchomu/data-for-yolo-v3-kernel")
print("Path to dataset files:", path)

weights_path = os.path.join(path, "yolov3.weights")
names_path = os.path.join(path, "coco.names")
config_path = "/content/yolov3.cfg"  


with open(names_path, "r") as f:
    classes = f.read().splitlines()

print(classes)


net = cv2.dnn.readNet(weights_path, config_path)

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]


img_path = os.path.join(path, "dog.jpg")
img = cv2.imread(img_path)

if img is None:
    print("Error: Image not found or path is incorrect")
    exit()

height, width, _ = img.shape


blob = cv2.dnn.blobFromImage(
    img, 1 / 255, (416, 416), swapRB=True, crop=False
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


indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

if len(indexes) > 0:
    for i in indexes:
        i = i[0] if isinstance(i, (list, tuple, np.ndarray)) else i
        x, y, w, h = boxes[i]
        label = classes[class_ids[i]]

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            img,
            label,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )
else:
    print("No boxes after NMS")

print("Boxes detected:", len(boxes))

cv2_imshow(img) 
cv2.waitKey(0)
cv2.destroyAllWindows()