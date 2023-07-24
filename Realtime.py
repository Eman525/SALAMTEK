import cv2
import argparse

import numpy as np
import supervision as cv
from ultralytics import YOLO
from PIL import Image
import numpy as np
from numpy import asarray
from skimage.transform import resize
ZONE_POLYGON = np.array([
    [0 , 0],
    [1280 , 0],
    [1250 , 720],
    [0 , 720]
])


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser ( description = "YOLOv8 live")
    parser.add_argument(
        "--webcam-resolution"
        , default = [640 , 640]
        , nargs = 2 , type = int
    )
    args = parser.parse_args()
    return args



def camira():

    args = parse_arguments()

    frame_width, frame_height = args.webcam_resolution

    cap = cv2.VideoCapture(0)

    #cap.set(cv2.CAP_PROP_FPS, 240)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    model = YOLO("best\\best.pt")

    box_annotator = cv.BoxAnnotator (
        thickness = 2 ,
        text_thickness= 2 ,
        text_scale = 1
    )
    zone = cv.PolygonZone(polygon=ZONE_POLYGON , frame_resolution_wh = tuple(args.webcam_resolution))
    zone_annotator = cv.PolygonZoneAnnotator (
        zone = zone ,
        color = cv.Color.red(),
        thickness = 0 ,
        text_thickness = 0,
        text_scale = 0
    )

    while True:
        ret, frame = cap.read()
        result = model(frame)[0]
        detections = cv.Detections.from_yolov8(result)
        frame = box_annotator.annotate(scene = frame , detections = detections ,)
        # zone.trigger(detections = detections)
        # frame = zone_annotator.annotate(scene=frame)
        cv2.imshow("yolov8" , frame)
        
        # esc button = 30
        if (cv2.waitKey(30) == 27):
           break

