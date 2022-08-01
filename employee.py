from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2

class Employee :
    def __init__(self, root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self. root.title("face Recogniton System ")
        self.root.attributes("-fullscreen", True)
        self.root.config(bg="#18191A")
        
        #variables
        
        self.emp_id = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.dept = StringVar()
        
        label1=Label(self.root, text='the HAWKEYE', fg='white', bg='#000') 
        label1.configure(font=("Game Of Squids", 24, "bold"), pady=10)  
        
        label1.place(x=0,y=0, width=1600)
        
        hawkeye_img_small=Image.open(r"D:\python\HawkEye\Assets\HawkEye-logo-dark.jpg")
        hawkeye_img_small=hawkeye_img_small.resize ( (60, 40), resample=Image.LANCZOS )
        self.photoimg_logo_small=ImageTk.PhotoImage(hawkeye_img_small)
        
        
        hawkeye_logo_small=Label (self.root, image=self.photoimg_logo_small, bg="black")
        hawkeye_logo_small.place(x=5, y=5, width=90, height=50)
        # Background Image
        bg_img=Image.open(r"C:\Users\VIVOBOOK 14\Downloads\HawkEye-logo.png")
        bg_img=bg_img.resize ( (530, 410), resample=Image.LANCZOS )
        self.photoimg=ImageTk.PhotoImage(bg_img)
        
        
        bg_lbl=Label (self. root, image=self.photoimg)
        bg_lbl.place(x=500, y=210, width=530, height=410)
        
        main_frame = Frame (self.root, bd=2, bg="#18191A")
        main_frame.place (x=20, y=100, width=1480, height =600)
        
        # Left label Frame
        Left_frame= LabelFrame (main_frame, bd=2, relief=RIDGE, text="Employee Details", bg='#18191A', fg="#ffffff")
        Left_frame. place(x=40, y=10, width=660, height =580)
        
        # current course
        current_course_frame=LabelFrame(Left_frame, bd=2,  relief=RIDGE, text="Personal Details",bg='#18191A', fg="#ffffff")
        current_course_frame.place(x=5,y=5, width=645, height=150)
        
        
        # Employee ID
        emp_id_label=Label(current_course_frame,  text="ID", font=("Sans Serif", 9),bg='#18191A', fg="#ffffff")
        emp_id_label.grid(row=0, column=0)
        
        emp_id_combo=ttk.Entry(current_course_frame,textvariable=self.emp_id, font=("Sans Serif", 12, "bold"),width=17) 
        emp_id_combo.grid(row=0, column=1, padx=10, pady= 3)
        
        # Employee name 
        emp_name_label=Label(current_course_frame,  text="Name ", font=("Sans Serif", 9),bg='#18191A', fg="#ffffff")
        emp_name_label.grid(row=0, column=2)
        
        emp_name_combo=ttk.Entry(current_course_frame,textvariable=self.name, font=("Sans Serif", 12, "bold"),width=17) 
        emp_name_combo.grid(row=0, column=3, padx=10, pady= 3)
        
         # Employee email 
        emp_email_label=Label(current_course_frame, text="E-Mail ", font=("Sans Serif", 9), fg="#ffffff",bg='#18191A')
        emp_email_label.grid(row=1, column=0, padx=3)
        
        emp_email_combo=ttk.Entry(current_course_frame,textvariable=self.email, font=("Sans Serif", 12, "bold"),width=17)
        emp_email_combo.grid(row=1, column=1, padx=10, pady= 10)
        
        
        # Department name 
        dep_label=Label(current_course_frame, text="Department ", font=("Sans Serif", 9), fg="#ffffff",bg='#18191A')
        dep_label.grid(row=1, column=2)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.dept, font=("Sans Serif", 12, "bold"),width=17, state="readonly", )
        
        dep_combo["values"]=("Select Department", "Computer", "IT")
        dep_combo.grid(row=1, column=3, padx=10, pady= 3)
                
       
        
        
        # # Sample Photo Frame
        # sample_photo_frame=LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Sample Photo")
        # sample_photo_frame.place(x=5,y=165, width=645, height=50)
        
        
        # # radio Buttons
        # radiobtn1=ttk. Radiobutton (sample_photo_frame, text="Take Photo Sample", value="Yes")
        # radiobtn1.grid(row=6, column=0)
        # radiobtn2=ttk. Radiobutton(sample_photo_frame, text="No Photo Sample", value= "No")
        # radiobtn2 .grid(row=6, column=1)
        
        # Button Frame
        button_frame=LabelFrame(Left_frame, bd=2,  relief=RIDGE, pady=15,bg='#18191A')
        button_frame.place(x=5,y=230, width=645, height=100)
        
        save_btn=Button (button_frame, command=self.add_data, text="Save", width=13, font= ("Sans Serif", 13, "bold ") ,bg='#3A3B3C', fg="#ffffff")
        save_btn.grid(row=0, column=0)
        
        update_btn=Button(button_frame, text="Update ",command=self.update_details, width=15, font=("Sans Serif",13, "bold"),bg='#3A3B3C', fg="#ffffff")
        update_btn.grid (row=0, column=1, padx=5)
        
        delete_btn=Button (button_frame, text= "Delete",command=self.delete_details, width=15, font= ("Sans Serif", 13, "bold"),bg='#3A3B3C', fg="#ffffff")
        delete_btn.grid (row=0, column=2, padx=5)
        
        reset_btn=Button (button_frame, text= "Reset", width=13, font=("Sans Serif", 13, "bold"),bg='#3A3B3C', fg="#ffffff")
        reset_btn.grid (row=0, column=3, padx=5)
        
        take_photo_btn=Button (button_frame, text= "Take Photo",command=self.generate_daraset, width=15, font=("Sans Serif", 13, "bold"),bg='#3A3B3C', fg="#ffffff")
        take_photo_btn.grid (row=1, column=1,pady=5, padx=5)
        
        update_photo_btn=Button (button_frame, text= "Update Photo", width=15, font=("Sans Serif", 13, "bold"),bg='#3A3B3C', fg="#ffffff")
        update_photo_btn.grid (row=1, column=2,pady=5, padx=5)
                
        
        
        
        # Right label Frame
        Right_frame= LabelFrame (main_frame, bd=2, relief=RIDGE, text="Employee Details",bg='#18191A', fg="#ffffff")
        Right_frame. place(x=760, y=10, width=660, height =580)

        search_box_frame=LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search By",bg='#18191A', fg="#ffffff")
        search_box_frame.place(x=5,y=5, width=645, height=150)
        
        search_combo=ttk.Combobox(search_box_frame, font=("Sans Serif", 12, "bold"),width=17, state="readonly", )
        
        search_combo["values"]=("Select Department", "Computer", "IT")
        search_combo.grid(row=0, column=1, padx=10, pady= 3)
        
        search_inp=ttk.Entry(search_box_frame, font=("Sans Serif", 12, "bold"),width=17)
        search_inp.grid(row=0, column=2, padx=10, pady= 10)
 
        reset_btn=Button (search_box_frame, text= "Search", width=15, font=("Sans Serif", 13, "bold"), bg="cyan", fg="black")
        reset_btn.grid (row=1, column=1, padx=5)
        
        take_photo_btn=Button (search_box_frame, text= "Show All", width=15, font=("Sans Serif", 13, "bold"), bg="cyan", fg="black")
        take_photo_btn.grid (row=1, column=2,pady=5, padx=5)
        
        # Back Button
        exit_btn=Button(self.root,command=self.go_back, text="Back", cursor="hand2", font=("Sans Serif", 15, "bold"))
        exit_btn.place (x=1300, y=750, width=180, height=40)
 
 
        data_display_frame = Frame(Right_frame, bd=2, relief=RIDGE,bg='#18191A')
        data_display_frame.place(x=2.5, y=210, width=650, height=347.5,)
        
        scroll_x = ttk.Scrollbar(data_display_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(data_display_frame, orient=VERTICAL)
        
        self.employee_data = ttk.Treeview(data_display_frame, columns=('ID','Name','E-Mail','Department'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_data.xview) 
        scroll_y.config(command=self.employee_data.yview)
        # self.employee_data.config(bg='#18191A', fg="#ffffff")
        self.employee_data.heading('ID', text="ID")
        self.employee_data.heading('Name', text="Name")
        self.employee_data.heading('E-Mail', text="E-Mail")
        self.employee_data.heading('Department', text="Department")
        self.employee_data.pack(fill=BOTH, expand=1)
        self.employee_data.bind("<ButtonRelease>", self.get_cursor)
        self.employee_data["show"]="headings"
        self.fetch_data()
        
    def go_back(self):
        self.root.destroy()
    
    def add_data(self):
        if self.dept.get()=="Select Department" or self.name.get()=='' or self.email.get()=='':
            messagebox.showerror("Error","All Fields Required.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hawkeye")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into employee (name,email,department) values(%s, %s, %s)", (self.name.get(), self.email.get(), self.dept.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Welcome User", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f'{str(e)}', parent= self.root)
                
                
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hawkeye")
        my_cursor = conn.cursor()
        my_cursor. execute ("select * from employee ")
        data=my_cursor.fetchall()
        if len (data) !=0:
            self.employee_data.delete(*self.employee_data.get_children ())
            for i in data:
                self.employee_data.insert ("", END, values =i)
            
            
        conn.commit()
        conn.close()
 
    def get_cursor (self, event):
        cursor_focus=self.employee_data.focus()
        content=self.employee_data.item(cursor_focus)
        data=content[ "values"]
        self.emp_id.set(data[0])
        self.name.set(data[1])
        self.email.set(data[2])
        self.dept.set(data[3])
        
    def update_details(self):
        if self.dept.get()=="Select Department" or self.name.get()=='' or self.email.get()=='':
            messagebox.showerror("Error","All Fields Required.", parent=self.root)
        else:
            
            confirm_update = messagebox.askyesno("Confirm Upadte","Do you wish to make the changes?", parent=self.root)
            if confirm_update>0:    
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hawkeye")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE employee SET name=%s, email=%s, department=%s WHERE emp_id=%s", (self.name.get(), self.email.get(), self.dept.get(), int(self.emp_id.get())))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Employee data updated.", parent=self.root)
                    
                except Exception as e:
                    messagebox.showerror("Error", f'{str(e)}', parent= self.root)
        
            else :
                return
 
    def delete_details(self):
      
        if self.emp_id.get() =="":
            messagebox.showerror ("Error", "Please select a record", parent=self.root)
        else:
            try:
                confirm_delete=messagebox.askyesno( "Confirm Delete", "Do you want to delete this record")
                if confirm_delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hawkeye")
                    my_cursor=conn.cursor()
                    my_cursor.execute("DELETE FROM employee WHERE emp_id=%s", (int(self.emp_id.get()),))
                    conn.commit()
                    messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
                    self.fetch_data()
                    conn.close()
                    
                else:
                    return
            except Exception as e:
                messagebox.showerror("Error", f"{e}")
        
        
        
    def generate_daraset(self):
        
        if self.dept.get()=="Select Department" or self.name.get()=='' or self.email.get()=='':
            messagebox.showerror("Error","All Fields Required.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hawkeye")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from employee")
                myresult=my_cursor.fetchall()
                # id=0
                # for x in myresult:
                #     id+=1
                my_cursor.execute("UPDATE employee SET name=%s, email=%s, department=%s WHERE emp_id=%s", (self.name.get(), self.email.get(), self.dept.get(), (int(self.emp_id.get()))))
                current_user = self.emp_id.get()
                conn.commit()
                self.fetch_data()
                conn.close()
                    
            
                face_classifier=cv2.CascadeClassifier ("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray, 1.3,5)
                    #scaling factor=1. 3
                    #Minimum Neighbor=5
                    for (x,y, w, h) in faces :
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        try:
                            face_resize=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face_resize, cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(current_user) + "."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path, face)
                        except Exception as e:
                            print(e)
                        cv2.putText (face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255,0), 2)
                        cv2.imshow ( "Cropped Face", face)
                    if cv2.waitKey(1) ==13 or img_id ==100 :
                        break
                cap.release ()
                cv2.destroyAllWindows ()
                messagebox.showinfo("Result", "Generating dataset complete.")
            except Exception as e:
                print(e)
                                            
                                    
        
if __name__ == "__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop ()