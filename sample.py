from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")
        
        #first image
        img=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\Stanford.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third image
        img2=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\u.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        #bg image
        img3=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #student button
        img4=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\student.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=80,y=80,width=200,height=200)
        
        b1_1=Button(bg_img,text="STUDENT DETAILS",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=80,y=280,width=200,height=30)
        
        #detect face button
        img5=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\face_detector1.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=350,y=80,width=200,height=200)
        
        b1_1=Button(bg_img,text="FACE DETECTOR",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=350,y=280,width=200,height=30)
        
        #ATTENDANCE face button
        img6=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\face_detector1.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=700,y=100,width=200,height=200)
        
        b1_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=300,width=200,height=30)
        
        #HELP DESK button
        img7=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\face_detector1.jpg")
        img7=img7.resize((200,290),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=1000,y=100,width=200,height=200)
        
        b1_1=Button(bg_img,text="HELP DESK",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=300,width=200,height=30)
        
        
        #Train  button
        img8=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\student.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=80,y=320,width=200,height=200)
        
        b1_1=Button(bg_img,text="TRAIN",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=80,y=510,width=200,height=30)
        
         #Train  button
        img8=Image.open(r"C:\Users\milin\Desktop\Face Recognition System\college_images\student.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=80,y=320,width=200,height=200)
        
        b1_1=Button(bg_img,text="TRAIN",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=80,y=810,width=200,height=30)
if __name__ == "__main__":
    root=Tk()
    object=Face_Recognition_System(root)
    root.mainloop()