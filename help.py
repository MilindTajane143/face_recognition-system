from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")
        
        
        title_lbl=Label(self.root,text="HELP DESK",font=("chiller",35,"bold"),bg="crimson",fg="chartreuse1")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        img_top=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1530,height=720)
        
        
        dev_label=Label(f_lbl,text=" Email:- milindtajane1@gmail.com",font=("times new roman",20,"bold"),bg="greenyellow")
        dev_label.place(x=550,y=190)
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    object=Help(root)
    root.mainloop()