from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import tkinter
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from chatbot import ChatBot
import pyttsx3



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0") #14 inch laptop resoultion (1920x1080+0+0)
        self.root.title("Face Recognition Attendance System")
        
        
        
        #first image
        img=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third image
        img2=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\images.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        #bg image
        img3=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        
        upper_lbl=Label(self.root,text="Developed By:-Milind Tajane",font=("algerian",10,"bold"),bg="black",fg="orange")
        upper_lbl.place(x=0,y=0,width=230,height=30)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        #time
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)
            
            
        lbl = Label(title_lbl, font=("times new roman",20,"bold"),background="black",foreground="greenyellow")
        lbl.place(x=5,y=-2,width=150,height=33)
        time()
        
        
        
        #student button
        img4=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\student.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,bd=5,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="STUDENT DETAILS",bd=5,command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        #detect face button
        img5=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,bd=5,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="FACE DETECTOR",bd=5,cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        #ATTENDANCE face button
        img6=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\attendance.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,bd=5,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="ATTENDANCE",bd=5,cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        # #HELP DESK button
        # img7=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\help.jpg")
        # img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        # self.photoimg7=ImageTk.PhotoImage(img7)
        
        # b1=Button(bg_img,bd=5,image=self.photoimg7,cursor="hand2",command=self.help_data)
        # b1.place(x=1100,y=100,width=220,height=220)
        
        # b1_1=Button(bg_img,text="HELP DESK",bd=5,cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b1_1.place(x=1100,y=300,width=220,height=40)
        
        #HELP DESK button
        img7=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\chat.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,bd=5,image=self.photoimg7,cursor="hand2",command=self.chatbot_data)
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="CHAT BOT",bd=5,cursor="hand2",command=self.chatbot_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        #Train  button
        img8=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\Train.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,bd=5,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="TRAIN DATA",bd=5,cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)
        
         #PHOTOS  button
        img9=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,bd=5,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="PHOTOS",bd=5,cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        #DEVELOPER  button
        img10=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,bd=5,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="DEVELOPER",bd=5,cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        #EXIT  button
        img11=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,bd=5,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="EXIT",bd=5,cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)
        
        
        #developer name
        lower_lbl=Label(self.root,text="Leadership Is The Ability To Facilitate Movement In The Needed Direction And Have People Feel Good About It..",font=("cooper black",15,"bold"),bg="white",fg="red")
        lower_lbl.place(x=0,y=675,width=1530,height=25)
     
    def open_img(self):
        os.startfile("data")
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("FACE RECOGNITION SYSTEM","ARE YOU WANT TO EXIT?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
       
    #Function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
        
    # def help_data(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Help(self.new_window)
        
    
    def chatbot_data(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)

        
        
if __name__ == "__main__":
    root=Tk()
    object=Face_Recognition_System(root)
    root.mainloop()
    