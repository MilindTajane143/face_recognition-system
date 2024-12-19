from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv 
from tkinter import filedialog


myData=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")
        
        
        #variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_department=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        #first image
        img=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\smart-attendance.jpg")
        img=img.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
        #second image
        img1=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\iStock-182059956_18390_t12.jpg")
        img1=img1.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
        upper_lbl=Label(self.root,text="Developed By:-Milind Tajane",font=("algerian",15,"bold"),bg="red",fg="greenyellow")
        upper_lbl.place(x=0,y=0,width=335,height=30)
        
        
        #bg image
        img3=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\un.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)
        
        #left label frame
        LEFT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"),fg="red")
        LEFT_frame.place(x=10,y=10,width=730,height=580)
        
        img_left=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(LEFT_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=720,height=130)
        
        
        left_inside_frame=Frame(LEFT_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=3,y=135,width=720,height=370)
        
        
        #label and entry
        #attendance ID
        attendanceID_label=Label(left_inside_frame,text=" ATTENDANCE ID:",font=("times new roman",13,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        
        #ROLL NO
        rollLabel=Label(left_inside_frame,text="ROLL NO:",font=("times new roman",13,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)
        
        rollLabel_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        rollLabel_entry.grid(row=0,column=3,pady=8)
        
        
        #NAME
        nameLabel=Label(left_inside_frame,text="NAME:",font=("times new roman",13,"bold"),bg="white")
        nameLabel.grid(row=1,column=0)
        
        nameLabel_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        nameLabel_entry.grid(row=1,column=1,pady=8)
        
        
        #department
        depLabel=Label(left_inside_frame,text="DEPARTMENT:",font=("times new roman",13,"bold"),bg="white")
        depLabel.grid(row=1,column=2)
        
        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_department,font=("times new roman",13,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)
        
        
        #TIME
        timeLabel=Label(left_inside_frame,text="TIME:",font=("times new roman",13,"bold"),bg="white")
        timeLabel.grid(row=2,column=0)
        
        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        atten_time.grid(row=2,column=1,pady=8)
        
        
        #DATE
        dateLabel=Label(left_inside_frame,text="DATE:",font=("times new roman",13,"bold"),bg="white")
        dateLabel.grid(row=2,column=2)
        
        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=3,pady=8)
        
        #attendance
        attendanceLabel=Label(left_inside_frame,text="ATTENDANCE STATUS:",font=("times new roman",13,"bold"),bg="white")
        attendanceLabel.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns  11 bold",state="readonly")
        self.atten_status["values"]=("STATUS","PRESENT","ABSENT")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        
        #BUTTON FRAME
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=42)
        
        
        import_btn=Button(btn_frame,text="IMPORT csv",command=self.fetch_data,bd=5,cursor="hand2",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)
        
        export_btn=Button(btn_frame,text="EXPORT csv",bd=5,cursor="hand2",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)
        
        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,bd=5,cursor="hand2",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,bd=5,cursor="hand2",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        
        
        #+++++++++++++right label frame++++++++++++++++
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),fg="red")
        RIGHT_frame.place(x=750,y=10,width=720,height=580)
        
        table_frame=Frame(RIGHT_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)
        
        img_right=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\student.jpg")
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
        search_combo["values"]=("SELECT ","roll","name","id")
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
        
        #scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="ATTENDANCE ID")
        self.AttendanceReportTable.heading("roll",text="ROLL NO") 
        self.AttendanceReportTable.heading("name",text="NAME")
        self.AttendanceReportTable.heading("department",text="DEPARTMENT")
        self.AttendanceReportTable.heading("time",text="TIME")
        self.AttendanceReportTable.heading("date",text="DATE")
        self.AttendanceReportTable.heading("attendance",text="ATTENDANCE")
        self.AttendanceReportTable["show"]="headings"
        
         
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100) 
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.attendancereporttable.pack(fill=BOTH,expand=1)
        self.attendancereporttable.bind("<ButtonRelease>",self.get_cursor)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
             
    #fetch data
    
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
        
    #import csv
    def importCsv(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)
            
            
    #export csv
    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("NO DATA","NO DATA FOUND TO EXPORT",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("DATA EXPORT","YOUR DATA EXPORTED TO   "+os.path.basename(fln)+"  SUCCESSFULLY")
        except Exception as es:
                messagebox.showerror("ERROR",f"DUE TO :{str(es)}",parent=self.root)
                
    def get_cursor(self,event=""):
        cursor_row=self.attendancereporttable.focus()
        content=self.attendancereporttable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_department.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
        
        
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_department.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
                
        
if __name__ == "__main__":
    root=Tk()
    object=Attendance(root)
    root.mainloop()