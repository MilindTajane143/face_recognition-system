from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


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
        frame=Frame(self.root,bg="greenyellow")
        frame.place(x=520,y=100,width=800,height=550)
        
        
        #register label
        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),bg="greenyellow",fg="darkorange")
        register_lbl.place(x=20,y=20)
        
        
        #labels and entrys
        
        #row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="greenyellow")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50,y=130,width=250)
        
        l_name=lbl=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="greenyellow")
        l_name.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #row 2
        contact=lbl=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="greenyellow")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="greenyellow")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        
        #row 3
        security_Q=lbl=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="greenyellow")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","What Is Your Birth Place?","What Is Your Birth Date?","What Is Your Pet Name?","What Is Your Bike No?","Which Is Your Favourite Dish?")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="greenyellow",fg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
        
        
        #row 4
        pswd=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="greenyellow")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=lbl=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="greenyellow")
        confirm_pswd.place(x=370,y=310)
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        
        #check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),bg="greenyellow",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        #buttons
        img=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\register-now-button1-removebg-preview.png")
        img=img.resize((200,45),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=4,cursor="hand2")
        b1.place(x=70,y=420,width=200)
        
        
        #buttons
        img1=Image.open(r"C:\Users\MILIND TAJANE\Desktop\Face Recognition System\college_images\loginpng.png")
        img1=img1.resize((200,45),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=4,cursor="hand2")
        b1.place(x=400,y=420,width=200)
        
        
        
        
    #function declearation
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields Are Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password Must Be Same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms And Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="HyTwPNXLQpYc3bn",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone() 
            if row!=None:
                messagebox.showerror("Error","User Already Exist,Please Try Another Email")
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
            
            
        
        
if __name__ == "__main__":
    root=Tk()
    object=Register(root)
    root.mainloop()