from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
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



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Login Window")
        
        
        #bg image
        img9=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\2-AI-invades-automobile-industry-in-2019.jpeg")
        img9=img9.resize((1530,715),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        bg_img=Label(self.root,image=self.photoimg9)
        bg_img.place(x=0,y=0,width=1530,height=715)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM ",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=128,width=1530,height=30)
        
        lower_lbl=Label(bg_img,text="Note:-Please Enter Valid Username & valid Password",font=("times new roman",30,"bold"),bg="white",fg="blue")
        lower_lbl.place(x=0,y=665,width=1530,height=33)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        
        #first image
        img=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\facial-recognition_0.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)
        
        #second image
        img1=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=500,height=130)
        
        #third image
        img8=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\smart-attendance.jpg")
        img8=img8.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        f_lbl=Label(self.root,image=self.photoimg8)
        f_lbl.place(x=900,y=0,width=500,height=130)
        
        upper_lbl=Label(self.root,text="Developed By:-Milind Tajane",font=("algerian",15,"bold"),bg="white",fg="orange")
        upper_lbl.place(x=0,y=0,width=335,height=30)
        
        # ℳÎ£Î₦Ð ₮₳ʝ₳₦Ę
        
        #center image
        img2=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\LoginIconAppl.png")
        img2=img2.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg2.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("times new romman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,show="■",font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        
        #icon images
        img3=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\LoginIconAppl.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=323,width=25,height=25)
        
        img4=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\lock-512.png")
        img4=img4.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg4=Label(image=self.photoimg4,bg="black",borderwidth=0)
        lblimg4.place(x=650,y=393,width=25,height=25)
        
        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="red",activebackground="greenyellow")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #register button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",13,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
        
        #forget button
        btn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",13,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        btn.place(x=10,y=375,width=160)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def login(self):
        if self.txtuser.get()==""or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Required")
        elif self.txtuser.get()=="milind@8551" and self.txtpass.get()=="1739":
            messagebox.showinfo("Success","Welcome to Face Recognition System Software")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="HyTwPNXLQpYc3bn",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                      self.txtuser.get(),
                                                                                      self.txtpass.get()
                                                                            ))
            row=my_cursor.fetchone()
            
            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("Permission","Access Only Autority Person")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
    #reset password====================
    def reset_pass(self):
        if self.combo_securityQ.get()=="Select":
            messagebox.showerror("Error","Select The Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter The Password",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter The New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="HyTwPNXLQpYc3bn",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_securityQ.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Error","Your Password Has Been Reset Successfully,Please Login With New Password",parent=self.root2)
                self.root2.destroy()
            
        
            
        
            
    # forgot password=================        
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter Email To Reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="HyTwPNXLQpYc3bn",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            
            if row==None:
                messagebox.showerror("Error","Please Enter Valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)
                
                security_Q=lbl=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)
                
                self.combo_securityQ=ttk.Combobox(self.root2,font=("times new roman",15),state="readonly")
                self.combo_securityQ["values"]=("Select","What Is Your Birth Place?","What Is Your Pet Name?","What Is Your Bike No?","Which Is Your Favourite Dish?")
                self.combo_securityQ.place(x=50,y=110,width=250)
                self.combo_securityQ.current(0)
                
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)
                
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)
                
                
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)
                
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="green",fg="white")
                btn.place(x=100,y=290)
        
            
    
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1920x1080+0+0")
        
        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        
        #right image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\Screenshot_20221219_132215.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        #left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\facerecog.png")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        
        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        
        #register label
        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="darkorange")
        register_lbl.place(x=20,y=20)
        
        
        #labels and entrys
        
        #row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50,y=130,width=250)
        
        l_name=lbl=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #row 2
        contact=lbl=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        
        #row 3
        security_Q=lbl=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","What Is Your Birth Place?","What Is Your Pet Name?","What Is Your Bike No?","Which Is Your Favourite Dish?")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
        
        
        #row 4
        pswd=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=lbl=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=370,y=310)
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        
        #check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        #buttons
        img=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\register-now-button1.jpg")
        img=img.resize((200,55),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=70,y=420,width=200)
        
        
        #buttons
        img1=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\loginpng.png")
        img1=img1.resize((200,45),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=400,y=420,width=200)
        
        
        
        
    #function declearation
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password Must Be Same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms And Conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="HyTwPNXLQpYc3bn",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone() 
            if row!=None:
                messagebox.showerror("Error","User Already Exist,Please Try Another Email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                        
                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration Done Successfully")
            
    def return_login(self):
        self.root.destroy()
            
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        
        #first image
        img=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)
        
        #second image
        img1=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=500,height=130)
        
        #third image
        img2=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\images.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=500,height=130)
        
        #bg image
        img3=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("Chiller",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        #time
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)
            
            
        lbl = Label(title_lbl, font=("times new roman",20,"bold"),background="black",foreground="greenyellow")
        lbl.place(x=5,y=-5,width=150,height=50)
        time()
        
        
        
        #student button
        img4=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\student.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,bd=5,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=80,y=80,width=220,height=220)
        
        b1_1=Button(bg_img,text="STUDENT DETAILS",bd=5,command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=80,y=260,width=220,height=40)
        
        #detect face button
        img5=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,bd=5,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=380,y=80,width=220,height=220)
        
        b1_1=Button(bg_img,text="FACE DETECTOR",bd=5,cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=380,y=260,width=220,height=40)
        
        #ATTENDANCE face button
        img6=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\attendance.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,bd=5,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=680,y=80,width=220,height=220)
        
        b1_1=Button(bg_img,text="ATTENDANCE",bd=5,cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=680,y=260,width=220,height=40)
        
        # #HELP DESK button
        # img7=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\help.jpg")
        # img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        # self.photoimg7=ImageTk.PhotoImage(img7)
        
        # b1=Button(bg_img,bd=5,image=self.photoimg7,cursor="hand2",command=self.help_data)
        # b1.place(x=980,y=80,width=220,height=220)
        
        # b1_1=Button(bg_img,text="HELP DESK",bd=5,cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b1_1.place(x=980,y=260,width=220,height=40)
        
        #HELP DESK button
        img7=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\chat.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,bd=5,image=self.photoimg7,cursor="hand2",command=self.chatbot_data)
        b1.place(x=980,y=80,width=220,height=220)
        
        b1_1=Button(bg_img,text="CHAT BOT",bd=5,cursor="hand2",command=self.chatbot_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=980,y=260,width=220,height=40)
        
        
        #Train  button
        img8=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\Train.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,bd=5,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=80,y=320,width=220,height=220)
        
        b1_1=Button(bg_img,text="TRAIN DATA",bd=5,cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=80,y=510,width=220,height=40)
        
         #PHOTOS  button
        img9=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,bd=5,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=380,y=320,width=220,height=220)
        
        b1_1=Button(bg_img,text="PHOTOS",bd=5,cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=380,y=510,width=220,height=40)
        
        #DEVELOPER  button
        img10=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,bd=5,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=680,y=320,width=220,height=220)
        
        b1_1=Button(bg_img,text="DEVELOPER",bd=5,cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=680,y=510,width=220,height=40)
        
        #EXIT  button
        img11=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,bd=5,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=980,y=320,width=220,height=220)
        
        b1_1=Button(bg_img,text="EXIT",bd=5,cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=980,y=510,width=220,height=40)
     
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
    main()