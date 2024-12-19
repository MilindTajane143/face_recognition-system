from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import csv
from attendance import Attendance
from tkinter import filedialog
import pyttsx3


class Face_Recognition:
    
    
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")
        
        title_lbl=Label(self.root,text="Face Recognition ",font=("algerian",35,"bold"),bg="orange",fg="blueviolet")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #1st image
        img_top=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\face_detector1.jpg")
        img_top=img_top.resize((650,700),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=650,height=700)
        
        
        #2nd image
        img_bottom=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom=img_bottom.resize((950,700),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=45,width=950,height=700)
        
        #button
        back=Button(f_lbl,text="Back",command=self.root.destroy,bd=4,cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="white")
        back.place(x=35,y=100,width=150,height=30)
        #button
        b1_1=Button(f_lbl,text="Face Recognition",bd=4,cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="red",fg="white")
        b1_1.place(x=365,y=615,width=200,height=40)
        
        engine = pyttsx3.init()
        engine.say("Hi welcome to face recognition software")
        engine.runAndWait()
     #attendance
    def mark_attendance(self,i,r,n,d):
        
         
        now = datetime.now()
        curr_date = now.strftime("%d-%m-%Y")
       
        # with open(r"C:\Users\MILIND TAJANE\Desktop\face_recognition system\Attendance Data\Attendance Register-"+curr_date+".csv","w+") as f:
        #     myDataList=f.writable()  #+curr_date+".csv"
        with open(r"C:\Users\MILIND TAJANE\Desktop\face_recognition system\Attendance Data\Attendance Register-"+curr_date+".csv","w+") as f:
            myDataList=f.readlines()  #+curr_date+".csv"
            name_List=[]
            for line in myDataList:
                entry=line.split((","))
                name_List.append(entry[0])
            if((d not in name_List)(dtString not in name_List)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M")
                f.writelines(f"\n{i},{r},{n},{d},PRESENT")
                
                
    # with open(r"C:\Users\MILIND TAJANE\Desktop\face_recognition system\Attendance Data\Attendance Register-"+curr_date+".csv","r+") as f:
    #         myDataList=f.readlines()  #+curr_date+".csv"
    #         name_List=[]
    #         for line in myDataList:
    #             entry=line.split((","))
    #             name_List.append(entry[0])
    #         if((i not in name_List) and (r not in name_List) and (n not in name_List) and (d not in name_List)):
    #             now=datetime.now()
    #             d1=now.strftime("%d/%m/%Y")
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},PRESENT")
    #face recognition
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            
            coord=[]
            
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                
                conn=mysql.connector.connect(host="localhost",username="root",password="HyTwPNXLQpYc3bn",database="face_recognizer")
                my_cursor=conn.cursor()
                
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                
                
                if confidence>65:
                    cv2.putText(img,f"Id:{i}",(x,y-88),cv2.FONT_HERSHEY_COMPLEX,0.8,(25,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-65),cv2.FONT_HERSHEY_COMPLEX,0.8,(25,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(25,25,25),3)
                    cv2.putText(img,f"Department:{d}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(25,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"UNKNOWN FACE DETECTED",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,y]
                
            return coord
        
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNITION",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

                    
                    
if __name__ == "__main__":
    root=Tk()
    object=Face_Recognition(root)
    root.mainloop()