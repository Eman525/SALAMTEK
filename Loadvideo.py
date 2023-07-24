import cv2

import argparse
import tkinter as tk
from tkinter import filedialog
import numpy as np
import supervision as cv
from ultralytics import YOLO
from PIL import Image
import numpy as np
from numpy import asarray
from skimage.transform import resize

def load_video():
     model = YOLO("best\\best.pt")
     root = tk.Tk()
     root.withdraw()
     file_pathh = filedialog.askopenfilename(title='Select a video file', filetypes=[('Video files', '*.mp4 *.avi')])
     print('Selected file:', file_pathh)
     out_dec= model.predict(source=file_pathh,conf=.25,save=True)
     ######################################################
     





