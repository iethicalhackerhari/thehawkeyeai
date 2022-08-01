import threading
import email
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import  numpy as np
from emailer import Mail
from datetime import datetime


class Face_Recognizer:
    recently_recognised_faces =[]
    fetched_email=''
    def __init__(self, root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self. root.title("face Recogniton System ")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#18191A")
        
        
        label1=Label(self.root, text='the HAWKEYE', fg='white', bg='#000') 
        label1.configure(font=("Game Of Squids", 24, "bold"), pady=10)  
        
        label1.place(x=0,y=0, width=1600)
        hawkeye_img_small=Image.open(r"D:\python\HawkEye\Assets\HawkEye-logo-dark.jpg")
        hawkeye_img_small=hawkeye_img_small.resize ( (60, 40), resample=Image.LANCZOS )
        self.photoimg_logo_small=ImageTk.PhotoImage(hawkeye_img_small)
        
        
        hawkeye_logo_small=Label (self.root, image=self.photoimg_logo_small, bg="black")
        hawkeye_logo_small.place(x=5, y=5, width=90, height=50)
        btn_train = Button(root, text="Face Recognizer", command=self.face_recog )
        btn_train.place(x=200, y=200)
        # Back Button
        exit_btn=Button(self.root,command=self.go_back, text="Back", cursor="hand2", font=("times new roman", 15, "bold"))
        exit_btn.place (x=1300, y=750, width=180, height=40)
        
    
    def go_back(self):
        self.root.destroy()
        
    def face_recog(self):
        def draw_boundray(img, classifier, scale_factor, min_neighbours, color, text, classiFier) :
            gray_image=0
            features=[]
            
            try:
                gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image, scale_factor, min_neighbours)
            except Exception as e:
                print(e)
            
            coord=[]
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255,0),3)
                id, prediction=classiFier.predict(gray_image[y:y+h, x:x+w])
                confidence=int((100* (1-prediction/300)))
                
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hawkeye")
                my_cursor = conn.cursor()
                
                my_cursor.execute("SELECT name from employee WHERE emp_id="+str(id))
                fetch_name=my_cursor.fetchone()
                fetch_name='+'.join(fetch_name)
                
                my_cursor.execute("SELECT email from employee WHERE emp_id="+str(id))
                self.fetched_email=my_cursor.fetchone()
                
                if(self.fetched_email not in self.recently_recognised_faces):
                    self.recently_recognised_faces.append(self.fetched_email)

                # if (fetch_email in self.recently_recognised_faces):
                #     print(fetch_email in self.recently_recognised_faces)
                #     print('recently recognised')
                # else:
                #     if (fetch_email not in self.recently_recognised_faces):
                #         self.recently_recognised_faces.append(fetch_email[0])
                #         print(self.recently_recognised_faces)
                #         print(fetch_email[0])
                
                
                
                if confidence> 77:
                    cv2.putText(img, f"Name : {fetch_name}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0,0),3)
                else:
                    cv2.rectangle (img ,(x, y), (x+w, y+h), (0,0, 255), 3)
                    cv2. putText(img, "Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,0,0),3)
                coord=[x,y,w,h]
                    
            return  coord
        '''
            recieves one email and check for breach if the email is not recently checked
            current checking time is updated in the db
            
        '''
        
        def check_breach(email):
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hawkeye")
            my_cursor = conn.cursor()
            
            # checking if the email is recently checked
            now= datetime.now()
            current_time = now.strftime("%H:%M:%S")  
            
            my_cursor.execute("SELECT last_updated from breach WHERE email=%s", (str(email[0]),))
            last_updated= my_cursor.fetchone()
            
            last_updated_time = datetime.strptime(last_updated[0],"%H:%M:%S")
            current_time_time = datetime.strptime(current_time,"%H:%M:%S")
            print(current_time_time-last_updated_time)
            time_in_seconds = (current_time_time-last_updated_time).total_seconds()
            if  time_in_seconds > 100:
                print('30min ago')
                
                my_cursor.execute("SELECT isBreached from breach WHERE email=%s", (str(email[0]),))
                is_breached=my_cursor.fetchone()
                # mail_new= Mail()
                print(is_breached)
                if is_breached[0] == 1:
                     target= Mail(emails= email,subject= 'hi',content= 'BREACHED')
                     target.start()
                elif is_breached[0] == 0:
                     target= Mail(emails= email,subject= 'hi',content= 'BREACHED')
                     target.start()
                    
                    
                    
                    
                
                my_cursor.execute("UPDATE breach SET last_updated =%s WHERE email=%s", (str(current_time),str(email[0])))
                conn.commit()
                
                # print(str(email[0]))
                
                conn.close()
            
            else:
                print('less than 30 mins')
            
            
            
        def recognize (img, classiFier, faceCascade) :
            coord=draw_boundray(img, faceCascade, 1.1, 10,(255, 255, 255), "Face",classiFier)
            # conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hawkeye")
            # my_cursor = conn.cursor()
            # my_cursor.execute("SELECT email from employee WHERE emp_id="+str(id))
            # self.fetched_email=my_cursor.fetchone()
            
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        classiFier=cv2.face.LBPHFaceRecognizer_create()
        classiFier.read("classifier.xml")
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret, frame=video_cap.read()
            frame=recognize(frame, classiFier, faceCascade)
        
            cv2.imshow( "Welcome To face Recognition", frame)
            if cv2.waitKey(1)==13 :
                break
        # print(self.recently_recognised_faces)
        
            for faces in self.recently_recognised_faces:           
                check_breach(faces)
        video_cap.release()
        cv2.destroyAllWindows()
        

        
            
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognizer(root)
    root.mainloop ()