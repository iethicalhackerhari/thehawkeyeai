from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import  numpy as np

class Train :
    def __init__(self, root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self. root.title("face Recogniton System ")
        self.root.configure(bg="#18191A")
        self.root.attributes("-fullscreen", True)
        
        btn_train = Button(root, text="Train" , command=self.train_classifier, font=("Sans Serif", 15, "bold"))
        btn_train.place(x=200, y=200, width=80, height=35)
        label1=Label(self.root, text='the HAWKEYE', fg='white', bg='#000') 
        label1.configure(font=("Game Of Squids", 24, "bold"), pady=10)  
        
        label1.place(x=0,y=0, width=1600)
        hawkeye_img_small=Image.open(r"D:\python\HawkEye\Assets\HawkEye-logo-dark.jpg")
        hawkeye_img_small=hawkeye_img_small.resize ( (60, 40), resample=Image.LANCZOS )
        self.photoimg_logo_small=ImageTk.PhotoImage(hawkeye_img_small)
        
        
        hawkeye_logo_small=Label (self.root, image=self.photoimg_logo_small, bg="black")
        hawkeye_logo_small.place(x=5, y=5, width=90, height=50)
        
    # Back Button
        exit_btn=Button(self.root,command=self.go_back, text="Back", cursor="hand2", font=("times new roman", 15, "bold"))
        exit_btn.place (x=1300, y=750, width=180, height=40)
        
    
    def go_back(self):
        self.root.destroy()
        
    def train_classifier ( self):
        data_dir=("data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir) ]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert ("L") #Gray scale image
            imageNp=np.array(img, 'uint8')
            id=int(os.path.split(image)[1].split(".")[1])
                                                         
            faces.append(imageNp)
            ids.append (id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey (1) == 13
        ids=np.array(ids)
        
        classiFier = cv2.face.LBPHFaceRecognizer_create()
        classiFier.train(faces, ids)
        classiFier.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success", "Training completed.")
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop ()