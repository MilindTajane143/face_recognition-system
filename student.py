from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import pyttsx3


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")
        
       
        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        #first image
        img=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\face-recognition.png")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\university.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third image
        img2=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\clg.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
         #bg image
        img3=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\hackers2.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=-2,y=-2,width=1530,height=33)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)
        
        #button
        back=Button(f_lbl,text="Back",command=self.root.destroy,bd=4,cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="white")
        back.place(x=35,y=100,width=150,height=30)
        
        #time
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)
            
        engine = pyttsx3.init()
        engine.say("Here you can add delete update student details and and find student details")
        engine.runAndWait()
            
            
        lbl = Label(title_lbl, font=("times new roman",20,"bold"),background="black",foreground="greenyellow")
        lbl.place(x=5,y=-2,width=150,height=33)
        time()
        
        #left label frame
        LEFT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"),fg="red")
        LEFT_frame.place(x=10,y=10,width=730,height=580)
        
        
        #student column image
        img_left=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(LEFT_frame,image=self.photoimg_left,bd=8)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        #current course
        current_course_frame=LabelFrame(LEFT_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"),fg="green")
        current_course_frame.place(x=5,y=135,width=720,height=125)
        
        #Department
        dep_label=Label(current_course_frame,text="DEPARTMENT",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("SELECT DEPARTMENT","IT","COMPUTER SCIENCE","B.M.S","CEVIL","MECHANICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
        #Course
        course_label=Label(current_course_frame,text="COURSE",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("SELECT COURSE","FY","SY","TY")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
         #YEAR
        year_label=Label(current_course_frame,text="YEAR",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("SELECT YEAR","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        #Semester
        semester_label=Label(current_course_frame,text="SEMESTER",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("SELECT SEMESTER","SEMESTER-1","SEMESTER-2","SEMESTER-3","SEMESTER-4","SEMESTER-5","SEMESTER-6")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #CLASS STUDENT INFORMATION
        class_student_frame=LabelFrame(LEFT_frame,bd=2,bg="white",relief=RIDGE,text="Student Class Information",font=("times new roman",12,"bold"),fg="green")
        class_student_frame.place(x=5,y=20,width=720,height=300)
        
        #student ID
        studentID_label=Label(class_student_frame,text="STUDENT ID:",font=("times new roman",13,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5, sticky=W)
        
        
        #student NAME
        studentname_label=Label(class_student_frame,text="STUDENT NAME:",font=("times new roman",13,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        
        #Class DIVISION
        class_div_label=Label(class_student_frame,text="DIVISION:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=18)
        div_combo["values"]=("SELECT DIVISION","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        #ROLL NO.
        roll_no_label=Label(class_student_frame,text="ROLL NO:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
        #GENDER
        gender_label=Label(class_student_frame,text="GENDER:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("SELECT GENDER","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        
        #DATE OF BIRTH
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        #EMAIL
        email_label=Label(class_student_frame,text="EMAIL:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
         #PHONE NO.
        phone_label=Label(class_student_frame,text="PHONE NO.:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        
         #ADDRESS
        address_label=Label(class_student_frame,text="ADDRESS:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        
         #Teacher Name
        teacher_label=Label(class_student_frame,text="TEACHER NAME:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        
        #RADIO1 BUTTONS
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="TAKE A PHOTO SAMPLE",value="YES")
        radiobtn1.grid(row=6,column=0,padx=10)
        
        
        #RADIO2 BUTTONS
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="NO PHOTO SAMPLE",value="NO")
        radiobtn2.grid(row=6,column=1,padx=5)
        
        #BUTTON FRAME
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)
        
        
        save_btn=Button(btn_frame,text="SAVE",bd=4,cursor="hand2",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="UPDATE",bd=4,cursor="hand2",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="DELETE",bd=4,cursor="hand2",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="RESET",bd=4,cursor="hand2",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,bg="blue",fg="white",text="TAKE PHOTO SAMPLE",bd=4,cursor="hand2",width=35,font=("times new roman",13,"bold"))
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,command=self.generate_dataset,bg="blue",fg="white",text="UPDATE PHOTO SAMPLE",bd=4,cursor="hand2",width=35,font=("times new roman",13,"bold"))
        update_photo_btn.grid(row=0,column=1)
        
        
        
        #+++++++++++++right label frame++++++++++++++++
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),fg="red")
        RIGHT_frame.place(x=750,y=10,width=720,height=580)
        
        
        img_right=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\student.jpg")
        img_right=img_right.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(RIGHT_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        
        #================SEARCH SYSTEM===============
        search_frame=LabelFrame(RIGHT_frame,bd=2,bg="white",relief=RIDGE,text="View Student Details & Search System",font=("times new roman",12,"bold"),fg="green")
        search_frame.place(x=5,y=135,width=710,height=70)
        
        
        search_label=Label(search_frame,text=" SEARCH BY:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("SELECT ","Roll","Name","Student_id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
           
        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)  
                              
        
        search_btn=Button(search_frame,text="SEARCH",command=self.search_data,bd=4,cursor="hand2",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        searchshowAll_btn=Button(search_frame,command=self.fetch_data,text="SHOW ALL",bd=4,cursor="hand2",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        searchshowAll_btn.grid(row=0,column=4,padx=4)
        
        
        #============table frame==============
        table_frame=Frame(RIGHT_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("dep",text="DEPARTMENT")
        self.AttendanceReportTable.heading("course",text="COURSE") 
        self.AttendanceReportTable.heading("year",text="YEAR")
        self.AttendanceReportTable.heading("sem",text="SEMESTER")
        self.AttendanceReportTable.heading("id",text="STUDENT ID")
        self.AttendanceReportTable.heading("name",text="NAME")
        self.AttendanceReportTable.heading("div",text="DIVISION")
        self.AttendanceReportTable.heading("roll",text="ROLL NO")
        self.AttendanceReportTable.heading("gender",text="GENDER")
        self.AttendanceReportTable.heading("dob",text="DOB")
        self.AttendanceReportTable.heading("email",text="EMAIL")
        self.AttendanceReportTable.heading("phone",text="PHONE NO")
        self.AttendanceReportTable.heading("address",text="ADDRESS")
        self.AttendanceReportTable.heading("teacher",text="TEACHER")
        self.AttendanceReportTable.heading("photo",text="PHOTO SAMPLE STATUS")
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("dep",width=140)
        self.AttendanceReportTable.column("course",width=80) 
        self.AttendanceReportTable.column("year",width=80)
        self.AttendanceReportTable.column("sem",width=100)
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("div",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("gender",width=100)
        self.AttendanceReportTable.column("dob",width=100)
        self.AttendanceReportTable.column("email",width=180)
        self.AttendanceReportTable.column("phone",width=100)
        self.AttendanceReportTable.column("address",width=100)
        self.AttendanceReportTable.column("teacher",width=150)
        self.AttendanceReportTable.column("photo",width=150)


        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #========FUNCTION DECLEARATION==========
    def add_data(self):
        if self.var_dep.get()=="SELECT DEPARTMENT" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="HyTwPNXLQpYc3bn",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                        self.var_dep.get(),
                                                                        self.var_course.get(),
                                                                        self.var_year.get(),
                                                                        self.var_semester.get(),
                                                                        self.var_std_id.get(),
                                                                        self.var_std_name.get(),
                                                                        self.var_div.get(),
                                                                        self.var_roll.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_dob.get(),
                                                                        self.var_email.get(),
                                                                        self.var_phone.get(),
                                                                        self.var_address.get(),
                                                                        self.var_teacher.get(),
                                                                        self.var_radio1.get()
                                                                
                                                                 ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS","STUDENT DETAILS HAS BEEN ADDED SUCCESSFULLY",parent=self.root)
            except Exception as es:
                messagebox.showerror("ERROR",f"DUE TO :{str(es)}",parent=self.root)
    #==============Fetch Data=======
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="HyTwPNXLQpYc3bn",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in data:
                self.AttendanceReportTable.insert("",END,values=i)
            conn.commit()
        conn.close()
    #=========get cursor=========
    def get_cursor(self,event=""):
        cursor_focus=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
    #UPDATE FUNCTION
    def update_data(self):
        if self.var_dep.get()=="SELECT DEPARTMENT" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("UPDATE","DO YOU WANT TO UPDATE THIS STUDENT DETAILS ?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="HyTwPNXLQpYc3bn",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()
        
                                                                                                                                                                                     ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("SUCCESS","STUDENT DATAILS HAS BEEN UPDATED SUCCESSFULLY",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()   
            except EXCEPTION as es:
                messagebox.showerror("ERROR",f"DUE TO:{str(es)}",parent=self.root)
       
    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("ERROR","STUDENT ID MUST BE REQUIRED",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("STUDENT DELETE PAGE","DO YOU WANT TO DELETE THIS STUDENT DATA ?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="HyTwPNXLQpYc3bn",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("DELETE","STUDENT DATA HAS BEEN DELETED SUCCESSFULLY",parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("ERROR",f"DUE TO:{str(es)}",parent=self.root)       
                
    #reset function
    def reset_data(self):
        self.var_dep.set("SELECT DEPARTMENT")
        self.var_course.set("SELECT COURSE")
        self.var_year.set("SELECT YEAR")
        self.var_semester.set("SELECT SEMESTER")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("SELECT DIVISION")
        self.var_roll.set("")
        self.var_gender.set("SELECT GENDER")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
    #search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please Select Option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="HyTwPNXLQpYc3bn",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()
                
                if len(rows)!=0:
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    for i in rows:
                        self.AttendanceReportTable.insert("",END,values=i)
                    
                    
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("ERROR",f"DUE TO :{str(es)}",parent=self.root)
                    
        
    #GENERATE DATA SET OR TAKE PHOTO SAMPLES
    def generate_dataset(self):
        if self.var_dep.get()=="SELECT DEPARTMENT" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="HyTwPNXLQpYc3bn",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()==id+1
        
                                                                                                                                                                                     ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #load predefined data on face frontals from opencv
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("CROOPED FACE",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("RESULT","GENERATING DATA SET COMPLETED SUCCESSFULLY")
            except EXCEPTION as es:
                messagebox.showerror("ERROR",f"DUE TO:{str(es)}",parent=self.root) 
    
          
        
if __name__ == "__main__":
    root=Tk()
    object=Student(root)
    root.mainloop()