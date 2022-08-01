from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from employee import Employee
from train import Train
from face_recognizer import Face_Recognizer
import os

class Face_Recognition_System :
    def __init__(self, root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.attributes("-fullscreen", True)
        self.root.title("face Recogniton System ")
        self.root.resizable(True, True)
        self.root.configure(bg="#18191A")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        # self.root.wm_attributes('-transparentcolor', 'grey')



        
        # Background Image
        bg_img=Image.open(r"D:\python\HawkEye\Assets\green.webp")
        bg_img=bg_img.resize ( (1600, 900), resample=Image.LANCZOS )
        self.photoimg=ImageTk.PhotoImage(bg_img)
        
        
        bg_lbl=Label (self. root, image=self.photoimg)
        # bg_lbl.place(x=0, y=0, width=1600, height=900)
        
        # Title
        # title = Label(self.root, text="Automatic Breach Detection System", font=(20))
        # title.place(x=0,y=0, width=1530, height=40)
        
        label1=Label(self.root, text='the HAWKEYE', fg='white', bg='#000') 
        label1.configure(font=("Game Of Squids", 24, "bold"), pady=10)  
        
        label1.place(x=0,y=0, width=1600)
 
 
        hawkeye_img_small=Image.open(r"D:\python\HawkEye\Assets\HawkEye-logo-dark.jpg")
        hawkeye_img_small=hawkeye_img_small.resize ( (60, 40), resample=Image.LANCZOS )
        self.photoimg_logo_small=ImageTk.PhotoImage(hawkeye_img_small)
        
        
        hawkeye_logo_small=Label (self.root, image=self.photoimg_logo_small, bg="black")
        hawkeye_logo_small.place(x=5, y=5, width=90, height=50)
 
 
        # Text on the left
        main_frame = Frame (self.root, bg='#18191A')
        main_frame.place (x=0, y=65, width=800, height =810)
        
        hawkeye_img=Image.open(r"D:\python\HawkEye\Assets\HawkEye-logo-small.png")
        hawkeye_img=hawkeye_img.resize ( (350, 200), resample=Image.LANCZOS )
        self.photoimg_logo=ImageTk.PhotoImage(hawkeye_img)
        
        
        hawkeye_logo=Label (main_frame, image=self.photoimg_logo, bg='#18191A')
        hawkeye_logo.place(x=120, y=80, width=350, height=200)
        
        
        text_h1 = Label(self.root, text="Your Intelligent Companion.", fg='white', bg='#18191A')
        text_h1.configure(font=("Montserrat", 24, "bold"), pady=10)  
        text_h1.place(x=100, y=330)
        
        text_p = Label(self.root, text="""
            Hawkeye is a threat intelligence system
            developed to minimize the attacks caused
            due to a email that has been a part of a
            data breach.
            
            This works using face detection and 
            searches for any breaches, if any 
            the user is notified via e-mail
                       """,fg='white', bg='#18191A')
        text_p.configure(font=("Montserrat", 18, "normal"), pady=10)  
        text_p.place(x=20, y=385)
 
 
        # Employee Button
        emp_img=Image.open(r".\Assets\user.webp")
        emp_img=emp_img.resize( (140, 140),  resample=Image.LANCZOS )
        self.photoimg1=ImageTk.PhotoImage(emp_img)
        
        emp__btn = Button( self.root,command=self.employee_details, image=self.photoimg1)
        emp__btn.place(x=1000,y=140+50, width=180, height=180)
        emp_1=Button( self.root,command=self.employee_details, text="Employee Details", cursor="hand2", font=("Sans Serif", 13, "bold"))
        emp_1.place (x=1000, y=300+50, width=180, height=40)
        
        # Face Recognition Button
        fr_img=Image.open(r".\Assets\face_recog.jpg")
        fr_img=fr_img.resize( (220, 220),  resample=Image.LANCZOS )
        self.photoimg2=ImageTk.PhotoImage(fr_img)
        
        fr__btn = Button(self.root,command=self.recognize, image=self.photoimg2)
        fr__btn.place(x=1300,y=140+50, width=180, height=180)
        fr_1=Button(self.root, text="Face Recognisation", command=self.recognize,cursor="hand2", font=("Sans Serif", 13, "bold"))
        fr_1.place (x=1300, y=300+50, width=180, height=40)
        
        # Train Button
        train_img=Image.open(r".\Assets\TRAIN.png")
        train_img=train_img.resize( (180, 180),  resample=Image.LANCZOS )
        self.photoimg3=ImageTk.PhotoImage(train_img)
        
        train__btn = Button(self.root,command=self.train_dataset, image=self.photoimg3)
        train__btn.place(x=1000,y=360+50, width=180, height=180)
        train_1=Button(self.root,command=self.train_dataset, text="Train", cursor="hand2", font=("Sans Serif", 13, "bold"))
        train_1.place (x=1000, y=520+50, width=180, height=40)
        
        # Photos Button
        photos_img=Image.open(r".\Assets\photos.webp")
        photos_img=photos_img.resize( (180, 180),  resample=Image.LANCZOS )
        self.photoimg4=ImageTk.PhotoImage(photos_img)
        
        photos__btn = Button(self.root, image=self.photoimg4)
        photos__btn.place(x=1300,y=360+50, width=180, height=180)
        photos_1=Button(self.root,command=self.open_photos, text="Photos", cursor="hand2", font=("Sans Serif", 13, "bold"))
        photos_1.place (x=1300, y=520+50, width=180, height=40)

        # Exit button
        
        exit_btn=Button(self.root,command=self.exit_application, text="Exit", cursor="hand2", font=("Sans Serif", 13, "bold"))
        exit_btn.place (x=1300, y=750, width=180, height=40)
        
 
    def employee_details (self) :
        self.new_window=Toplevel( self. root)
        self.app=Employee(self. new_window)
    
    def train_dataset (self) :
        self.new_window=Toplevel( self. root)
        self.app=Train(self. new_window)  
 

    def recognize (self) :
        self.new_window=Toplevel( self. root)
        self.app=Face_Recognizer(self. new_window) 
 
 
    def open_photos(self):
        os.startfile('data') 
      
    def exit_application(self):
        self.root.destroy() 
 
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop ()