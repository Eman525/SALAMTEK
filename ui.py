import tkinter as tk
import Loadvideo
import LoadImage
import Realtime
root = tk.Tk()
root.title("My App")
def loadimgg():
    LoadImage.img()
def video():
    Loadvideo.load_video()
def opencamira():
    Realtime.camira()    
#ui
##############################################################################################################################
bg_image = tk.PhotoImage(file="wepik-export-20230622063543V4zJ.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
root.minsize(800, 800)
root.maxsize(1000, 1000)
#button1
button1 = tk.Button(root, text="open camera", width=20, height=5)
button1.place(x=370, y=600, width=100, height=30)
button1.config(command=opencamira)

#button2
button2 = tk.Button(root, text="Load image", width=20, height=5)
button2.place(x=370, y=700, width=100, height=30)
button2.config(command=loadimgg)
#button3
button3 = tk.Button(root, text="Load video", width=20, height=5)
button3.place(x=370, y=500, width=100, height=30)
button3.config(command=video)




root.mainloop()