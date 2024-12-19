from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")
        
        
        title_lbl=Label(self.root,text="DEVELOPER INFORMATION",font=("times new roman",35,"bold"),bg="crimson",fg="chartreuse1")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        img_top=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\dev.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1530,height=720)
        
        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=700,y=0,width=500,height=600)
        
        
        img_top1=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\mkstyle.png")
        img_top1=img_top1.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)
        
        
        #developer info
        dev_label=Label(main_frame,text=" Hello My Name Is Milind Tajane",font=("times new roman",15,"bold"),bg="white",fg="orange")
        dev_label.place(x=0,y=5)
        
        dev_label=Label(main_frame,text=" I Am From SY.Bsc.CS FACULTY",font=("times new roman",15,"bold"),bg="white",fg="orange")
        dev_label.place(x=0,y=40)
        
        
        #third image
        img2=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2=img2.resize((500,390),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=390)
        
        

if __name__ == "__main__":
    root=Tk()
    object=Developer(root)
    root.mainloop()