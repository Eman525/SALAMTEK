import cv2
import os
import argparse
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import numpy as np
import supervision as cv
from ultralytics import YOLO
from PIL import Image
import numpy as np
from numpy import asarray
from skimage.transform import resize

def img():
     model = YOLO("best\\best.pt")
     dir_path = "runs\\detect"
     root = tk.Tk()
     root.withdraw()
     file_path = filedialog.askopenfilename(title='Select an image file', filetypes=[('Image files', '*.jpg *.jpeg *.png')])
     print('Selected file:', file_path)
    
     out_dec= model.predict(source=file_path,conf=.2,save=True)
     print(out_dec)
     
     #################### i take the number of folders
     file_list = os.listdir(dir_path)
     num_dirs = sum(os.path.isdir(os.path.join(dir_path, f)) for f in file_list)
     #########
     if num_dirs==1:
       num_dirs=""
     ############
     print(f"There are {num_dirs} directories in {dir_path}.")
     ###############################
     parts = file_path.rsplit("/", 1)
     imggg = Image.open(f"runs\\detect\\predict{num_dirs}\\{parts[1]}")
     #print(parts[1])
     imggg.show()




