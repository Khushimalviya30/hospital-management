import tkinter
from tkinter import messagebox
from tkinter import *
from sqlite3 import *

class Km():
    def main(self):
        try:
            self.k.destroy()
        except:
            pass
        self.k = Tk()
        self.k.geometry("1300x1100")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        self.frame1 = Frame(self.k,height=1100,width=1300)
        self.Bg=PhotoImage(file="BG.png")
        self.label = Label(self.frame1, image=self.Bg)
        self.label.place(x=0,y=0)
        self.frame1.pack(fill=BOTH,expand=1)
        
        #self.frame2 = Frame(self.k,height=500,width=1300)
        #self.plogo = PhotoImage(file="patientlogo.png")
        #self.dologo = PhotoImage(file="doc.png")
        #self.plogoc = self.plogo.subsample(2,2)
        #self.dologoc = self.dologo.subsample(2,2)
        
        #self.b1 = Button(image=self.plogoc)
        #self.b1.image = self.plogo
        #self.b2 = Button(image=self.dologoc)
        #self.b2.image = self.dologo
        self.button=Button(self.frame1,text= "PATIENT",cursor="hand2", bd=5 ,font=("cooper black",26, 'bold'),fg="red",bg="#0b1335",command=lambda:self.ppage())
        self.button.place(x=750,y=60)
        self.button1=Button(self.frame1,text= "DOCTOR",cursor="hand2", bd=5 ,font=("cooper black",26, 'bold'),fg="red",bg="#0b1335",command=lambda:self.dpage())
        self.button1.place(x=760,y=200)
        #self.b1.place(x=800,y=100)
        #self.b2.place(x=1000,y=100)
        #self.frame2.pack(fill=BOTH,expand=1)
        self.k.mainloop()

    def ppage(self):
        self.k.destroy()
        self.k = Tk()
        self.k.geometry("700x600")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        #self.Bg2=PhotoImage(file="")
        #self.label = Label(self.frame1, image=)
        #self.label.place(x=0,y=0)
        self.k.config(bg="light yellow")
        self.button2=Button(text= "BOOK APPOINTMENT", bd=5 ,font=("arial rounded mt",20, 'bold'),fg="red",bg="light blue",command=lambda:self.loginn())
        self.button2.place(x=190,y=200)
        
        self.button4=Button(text= "HOME PAGE", bd=5 ,font=("arial rounded mt",20, 'bold'),fg="red",bg="light blue",command=lambda:self.main())
        self.button4.place(x=250,y=400)

    def doc(self):
        self.k.destroy()
        self.k = Tk()
        self.k.geometry("1300x1100")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        self.k.config(bg="maroon")
        self.button11=Button(text= "Home",cursor="hand2" ,font=("cooper black",14, 'bold'),fg="red",bg="#0b1335",command=lambda:self.main())
        self.button11.place(x=1100,y=40)
        
        self.d1=PhotoImage(file="doc8.8.png")
        self.b5 = Button(image=self.d1,cursor="hand2",command=lambda:self.doc1())
        self.b5.place(x=50,y=100)
        self.l1 = Label(self.k,text="Cardiologist",bg="white",font=("arial",20))
        self.l1.place(x=80,y=358)
        
        self.d2=PhotoImage(file="doc10.png")
        self.b6 = Button(image=self.d2,cursor="hand2",command=lambda:self.doc2())
        self.b6.place(x=540,y=100)
        self.l2 = Label(self.k,text="Pathologist",bg="white",font=("arial",20))
        self.l2.place(x=570,y=356)
  
        self.d3=PhotoImage(file="doc9.9.png")
        self.b7 = Button(image=self.d3,cursor="hand2",command=lambda:self.doc3())
        self.b7.place(x=1000,y=100)
        self.l1 = Label(self.k,text="Oncologist",bg="white",font=("arial",20))
        self.l1.place(x=1034,y=358)

        self.d4=PhotoImage(file="doc7.7.png")
        self.b8 = Button(image=self.d4,cursor="hand2",command=lambda:self.doc4())
        self.b8.place(x=50,y=480)
        self.l1 = Label(self.k,text="Psychiatrist",bg="white",font=("arial",20))
        self.l1.place(x=80,y=735)

        self.d5=PhotoImage(file="doc5.5.png")
        self.b9 = Button(image=self.d5,cursor="hand2",command=lambda:self.doc5())
        self.b9.place(x=540,y=480)
        self.l1 = Label(self.k,text="Orthopedic Surgeon",bg="white",font=("arial",20))
        self.l1.place(x=531,y=735)

        self.d6=PhotoImage(file="doc6.png")
        self.b10 = Button(image=self.d6,cursor="hand2",command=lambda:self.doc6())
        self.b10.place(x=1000,y=480)
        self.l1 = Label(self.k,text="Dermatologist",bg="white",font=("arial",20))
        self.l1.place(x=1028,y=735)


    def register(self):
        self.k.destroy()
        self.k = Tk()
        self.k.geometry("1000x800")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        self.k.config(bg="brown")
        self.a=Label(self.k,text="Userame",bg="white",fg="blue",font=("arial",28))
        self.b=Label(self.k,text="Name",bg="white",fg="blue",font=("arial",28))
        self.c=Label(self.k,text="Mobile.No",bg="white",fg="blue",font=("arial",28))
        self.d=Label(self.k,text="Address",bg="white",fg="blue",font=("arial",28))
        self.e=Label(self.k,text="Gender",bg="white",fg="blue",font=("arial",28))
        self.v=IntVar()
        #Radiobutton(m,text="Male",variable=v,value=0).grid(row=12,column=2,padx=2)
        self.f=Radiobutton(text="Male",variable=self.v,value=0,font=("arial",28))
        self.g=Radiobutton(text="Female",variable=self.v,value=1,font=("arial",28))
        self.h=Label(self.k,text="Age",bg="white",fg="blue",font=("arial",28))
        
        self.a.place(x=80,y=100)
        self.b.place(x=80,y=200)
        self.c.place(x=80,y=300)
        self.d.place(x=80,y=400)
        self.e.place(x=80,y=500)
        self.f.place(x=500,y=495)
        self.g.place(x=700,y=495)
        self.h.place(x=80,y=600)
        self.e1=Entry(self.k,width=30,font=("arial",20))
        self.e2=Entry(self.k,width=30,font=("arial",20))
        self.e3=Entry(self.k,width=30,font=("arial",20))
        self.e4=Entry(self.k,width=30,font=("arial",20))
        self.e6=Entry(self.k,width=30,font=("arial",20))

        self.e1.place(x=500,y=100)
        #e1.pack()
        self.e2.place(x=500,y=200)
        self.e3.place(x=500,y=300)
        self.e4.place(x=500,y=400)
        self.e6.place(x=500,y=600)

        self.button11=Button(text= "Submit",cursor="hand2" ,font=("cooper black",18, 'bold'),fg="red",bg="#0b1335",command=lambda:self.reg_database())
        self.button11.place(x=500,y=700)

        self.button12=Button(text= "Back",cursor="hand2" ,font=("cooper black",18, 'bold'),fg="red",bg="#0b1335",command=lambda:self.ppage())
        self.button12.place(x=300,y=700)

    def resultreg(self):
        self.reguname=self.e1.get()
        self.regname=self.e2.get()
        self.regmob=self.e3.get()
        self.regaddr=self.e4.get()
        self.regage=self.e6.get()
        return self.reguname,self.regname,self.regmob,self.regaddr,self.regage

    def reg_database(self):
        self.credreg=self.resultreg()
        self.con=connect("appoint.db")
        self.cursor=self.con.cursor()
        try:
            self.cursor.execute("create table patient(username varchar(50) primary key,name varchar(50) not null,mob varchar(50) not null,address varchar(100), age varchar(5) not null)")
        except:
            pass
        x=self.cursor.execute("select count(*) from patient where username=%r and age=%r "%(self.credreg[0],self.credreg[4]))
        #print(x)
        if list(x)[0][0]==0:
            if self.credreg[0]=="" or self.credreg[1]=="" or self.credreg[2]=="" or self.credreg[4]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed(except Address)")
            else:
                self.cursor.execute("insert into patient values(%r,%r,%r,%r,%r)"%(self.credreg[0],self.credreg[1],self.credreg[2],self.credreg[3],self.credreg[4]))
                self.con.commit()
                messagebox.showinfo("Register","You are Successfully Registered")
                self.loginn()
        else:
            messagebox.showinfo("Register","Userame Already Exist \nEnter New Username")

    def loginn(self):
        self.k.destroy()
        self.k = Tk()
        self.k.geometry("1000x700")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        self.k.config(bg="brown")
        self.a1=Label(self.k,text="UserName",bg="white",fg="blue",font=("arial",28))
        self.b1=Label(self.k,text="Name",bg="white",fg="blue",font=("arial",28))
        self.c1=Label(self.k,text="Mobile No.",bg="white",fg="blue",font=("arial",28))

        self.a1.place(x=80,y=150)
        self.b1.place(x=80,y=250)
        self.c1.place(x=80,y=350)


        self.e7=Entry(self.k,width=30,font=("arial",20))
        self.e8=Entry(self.k,width=30,font=("arial",20))
        self.e9=Entry(self.k,width=30,font=("arial",20))

        self.e7.place(x=500,y=150)
        self.e8.place(x=500,y=250)
        self.e9.place(x=500,y=350)

        self.button13=Button(text= "Submit",cursor="hand2" ,font=("cooper black",18, 'bold'),fg="red",bg="#0b1335",command=lambda:self.log_database())
        self.button13.place(x=400,y=500)

        self.button11=Button(text= "Back",cursor="hand2" ,font=("cooper black",18, 'bold'),fg="red",bg="#0b1335",command=lambda:self.ppage())
        self.button11.place(x=550,y=600)

        self.button12=Button(text= "Register",cursor="hand2" ,font=("cooper black",18, 'bold'),fg="red",bg="#0b1335",command=lambda:self.register())
        self.button12.place(x=250,y=600)

    def resultlog(self):
        self.loguname=self.e7.get()
        self.logname=self.e8.get()
        self.logmob=self.e9.get()
        return self.loguname,self.logname,self.logmob

    def log_database(self):
        self.credlog=self.resultlog()
        self.con=connect("appoint.db")
        self.cursor=self.con.cursor()
        try:
            self.cursor.execute("create table patient(username varchar(50) primary key ,name varchar(50) not null,mob varchar(50) not null,address varchar(100), age varchar(5) not null)")
        except:
            pass
        x=self.cursor.execute("select count(*) from patient where username=%r and name=%r and mob=%r"%(self.credlog[0],self.credlog[1],self.credlog[2]))
        if list(x)[0][0]==0:
            if self.credlog[0]=="" or self.credlog[1]=="" or self.credlog[2]=="":
                messagebox.showinfo("Login","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Login","You are Not Registered Yet")
            
        else:
            messagebox.showinfo("Login","You have Successfully Log In")            
            self.doc()


    def doc1(self):
        self.k.destroy()
        self.k = Tk()
        self.k.geometry("900x800")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        self.k.config(bg="white")
        
        self.b1=Label(self.k,text="Dr.Gouri Rao",bg="white",fg="red",font=("arial",24))
        self.b1.place(x=50,y=100)
        self.b2=Label(self.k,text="Consultant Cardiologist",bg="white",fg="black",font=("arial",14))
        self.b2.place(x=50,y=140)
        self.b3=Label(self.k,text="Professional summary",bg="white",fg="red",font=("arial",24))
        self.b3.place(x=50,y=190)
        self.b4=Label(self.k,text="Dr.Gouri Rao has completed her M.B.B.S. from M G M Medical College, Indore and her M.D.\n in Medicine in year 1979 from Indore University, India.",bg="white",fg="black",font=("arial",14))
        self.b4.place(x=50,y=230)
        self.b5=Label(self.k,text="Technical Skills",bg="white",fg="red",font=("arial",24))
        self.b5.place(x=50,y=290)
        self.b6=Label(self.k,text="Pediatric cardiology\nInvasive Interventional cardiology\nPacing and Echocardiography\nEchocardiography",bg="white",fg="black",font=("arial",14))
        self.b6.place(x=50,y=330)
        self.b7=Label(self.k,text="Appointment",bg="white",fg="red",font=("arial",24))
        self.b7.place(x=50,y=450)
        self.b8=Label(self.k,text="WEDNESDAY & FRIDAY\n12:00 PM to 2:00 PM",bg="white",fg="black",font=("arial",14))
        self.b8.place(x=50,y=490)
        self.b9=Label(self.k,text="Book an Appointment",bg="white",fg="red",font=("arial",24))
        self.b9.place(x=50,y=550)
        self.b11=Label(self.k,text="Time",bg="white",fg="black",font=("arial",18))
        self.b11.place(x=50,y=600)
        self.e11 = Entry(self.k,width=10,font=("arial",14))
        self.e11.place(x=150,y=600)
        self.b12=Label(self.k,text="Date",bg="white",fg="black",font=("arial",18))
        self.b12.place(x=290,y=600)
        self.e12 = Entry(self.k,width=10,font=("arial",14))
        self.e12.place(x=400,y=600)
        self.b13=Label(self.k,text="Day",bg="white",fg="black",font=("arial",18))
        self.b13.place(x=540,y=600)
        self.e13 = Entry(self.k,width=10,font=("arial",14))
        self.e13.place(x=630,y=600)
        self.b14=Label(self.k,text="Appointment No.",bg="white",fg="black",font=("arial",18))
        self.b14.place(x=50,y=660)
        self.e14 = Entry(self.k,width=10,font=("arial",14))
        self.e14.place(x=250,y=660)
        self.b15=Label(self.k,text="Username",bg="white",fg="black",font=("arial",18))
        self.b15.place(x=400,y=660)
        self.e15 = Entry(self.k,width=20,font=("arial",14))
        self.e15.place(x=550,y=660)

        self.b1= Button(text= "Submit",cursor="hand2" ,font=("cooper black",14, 'bold'),fg="red",bg="#0b1335",command=lambda:self.doc1_database())
        self.b1.place(x=330,y=710)

        self.b2=Button(text= "Back",cursor="hand2" ,font=("cooper black",14, 'bold'),fg="red",bg="#0b1335",command=lambda:self.doc())
        self.b2.place(x=490,y=710)
        
        '''self.listbox=Listbox(self.k)
        self.listbox.place(x=50,y=490)
        self.listbox.insert(END,"Timing")
        for item in["10am to 12pm","1pm to 4pm","5pm to 9pm"]:
            self.listbox.insert(END,item)'''

    def resultdoc1(self):
        self.doc1ano=self.e14.get()
        self.doc1uname=self.e15.get()
        self.doc1time=self.e11.get()
        self.doc1date=self.e12.get()
        self.doc1day=self.e13.get()
        return self.doc1ano,self.doc1uname,self.doc1time,self.doc1date,self.doc1day


    def doc1_database(self):
        self.creddoc1=self.resultdoc1()
        self.con=connect("appoint.db")
        self.cursor=self.con.cursor()
        try:
            self.cursor.execute("create table doc1_patient(Appointment_no integer primary key autoincrement ,Username varchar(50) not null,Time varchar(30) not null, Date varchar(40) not null,Day varchar(40) not null)")
        except:
            pass
        x=self.cursor.execute("select count(*) from doc1_patient where Appointment_no=%r and Time=%r"%(self.creddoc1[0],self.creddoc1[2]))
        #print(x)
        if list(x)[0][0]==0:
            if self.creddoc1[0]=="" or self.creddoc1[1]=="" or self.creddoc1[2]=="" or self.creddoc1[3]=="" or self.creddoc1[4]=="":
                messagebox.showinfo("Invalid","Empty Entry is not Allowed")
            else:
                self.cursor.execute("insert into doc1_patient values(%r,%r,%r,%r,%r)"%(self.creddoc1[0],self.creddoc1[1],self.creddoc1[2],self.creddoc1[3],self.creddoc1[4]))
                self.con.commit()
                messagebox.showinfo("Book","You have Successfully Booked your Appointment")
                self.k.destroy()
        else:
            messagebox.showinfo("Book","One of the credentials already exist \nEnter again")

        
    def doc2(self):
        self.k.destroy()
        self.k = Tk()
        self.k.geometry("900x800")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        self.k.config(bg="white")
        
        self.b1=Label(self.k,text="Dr.Vidhut Kumar Jain",bg="white",fg="red",font=("arial",24))
        self.b1.place(x=50,y=100)
        self.b2=Label(self.k,text="Consultant Pathologist",bg="white",fg="black",font=("arial",14))
        self.b2.place(x=50,y=140)
        self.b7=Label(self.k,text="Appointment",bg="white",fg="red",font=("arial",24))
        self.b7.place(x=50,y=190)
        self.b8=Label(self.k,text="Monday(10:00 AM to 6:00 PM)\n\nTuesday(10:00 AM to 6:00 PM)\n\nWednesday(10:00 AM to 6:00 PM)\n\nThursday(10:00 AM to 6:00 PM)\n\nSaturday(10:00 AM to 6:00 PM)",bg="white",fg="black",font=("arial",14))
        self.b8.place(x=50,y=240)
        self.b9=Label(self.k,text="Book an Appointment",bg="white",fg="red",font=("arial",24))
        self.b9.place(x=50,y=550)
        self.b11=Label(self.k,text="Time",bg="white",fg="black",font=("arial",18))
        self.b11.place(x=50,y=600)
        self.e11 = Entry(self.k,width=10,font=("arial",14))
        self.e11.place(x=150,y=600)
        self.b12=Label(self.k,text="Date",bg="white",fg="black",font=("arial",18))
        self.b12.place(x=290,y=600)
        self.e12 = Entry(self.k,width=10,font=("arial",14))
        self.e12.place(x=400,y=600)
        self.b13=Label(self.k,text="Day",bg="white",fg="black",font=("arial",18))
        self.b13.place(x=540,y=600)
        self.e13 = Entry(self.k,width=10,font=("arial",14))
        self.e13.place(x=630,y=600)
        self.b14=Label(self.k,text="Appointment No.",bg="white",fg="black",font=("arial",18))
        self.b14.place(x=50,y=660)
        self.e14 = Entry(self.k,width=10,font=("arial",18))
        self.e14.place(x=250,y=660)
        self.b15=Label(self.k,text="Username",bg="white",fg="black",font=("arial",18))
        self.b15.place(x=400,y=660)
        self.e15 = Entry(self.k,width=20,font=("arial",14))
        self.e15.place(x=550,y=660)

        self.b1= Button(text= "Submit",cursor="hand2" ,font=("cooper black",14, 'bold'),fg="red",bg="#0b1335",command=lambda:self.doc2_database())
        self.b1.place(x=330,y=710)

        self.b2=Button(text= "Back",cursor="hand2" ,font=("cooper black",14, 'bold'),fg="red",bg="#0b1335",command=lambda:self.doc())
        self.b2.place(x=490,y=710)

    def resultdoc2(self):
        self.doc2ano=self.e14.get()
        self.doc2uname=self.e15.get()
        self.doc2time=self.e11.get()
        self.doc2date=self.e12.get()
        self.doc2day=self.e13.get()
        return self.doc2ano,self.doc2uname,self.doc2time,self.doc2date,self.doc2day

    def doc2_database():
        self.creddoc2=self.resultdoc2()
        self.con=connect("appoint.db")
        self.cursor=self.con.cursor()
        try:
            self.cursor.execute("create table doc2_patient(Appointment_no integer primary key autoincrement ,Username varchar(50) not null,Time varchar(30) not null, Date varchar(40) not null,Day varchar(40) not null)")
        except:
            pass
        x=self.cursor.execute("select count(*) from doc1_patient where Appointment_no=%r and Day=%r"%(self.creddoc2[0],self.creddoc2[4]))
        #print(x)
        if list(x)[0][0]==0:
            if self.creddoc2[0]=="" or self.creddoc2[1]=="" or self.creddoc2[2]=="" or self.creddoc2[3]=="" or self.creddoc2[4]=="":
                messagebox.showinfo("Invalid","Empty Entry is not Allowed")
            else:
                self.cursor.execute("insert into doc1_patient values(%r,%r,%r,%r,%r)"%(self.creddoc2[0],self.creddoc2[1],self.creddoc2[2],self.creddoc2[3],self.creddoc2[4]))
                self.con.commit()
                messagebox.showinfo("Book","You have Successfully Booked your Appointment")
                self.k.destroy()
        else:
            messagebox.showinfo("Book","One of the credentials already exist \nEnter again")

    def doc3(self):
        self.k.destroy()
        self.k = Tk()
        self.k.geometry("900x800")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        self.k.config(bg="white")
        
        self.b1=Label(self.k,text="Dr.Suresh Singh",bg="white",fg="red",font=("arial",24))
        self.b1.place(x=50,y=100)
        self.b2=Label(self.k,text="Consultant Radiation Oncology",bg="white",fg="black",font=("arial",14))
        self.b2.place(x=50,y=140)
        self.b3=Label(self.k,text="Professional summary",bg="white",fg="red",font=("arial",24))
        self.b3.place(x=50,y=190)
        self.b4=Label(self.k,text="Dr.Suresh Singh has completed his M.B.B.S. from S S Medical College and his M.D.\n in Radiotherapy from M G M Medical college,Indore in year 2004.",bg="white",fg="black",font=("arial",14))
        self.b4.place(x=50,y=230)
        self.b5=Label(self.k,text="Technical Skills",bg="white",fg="red",font=("arial",24))
        self.b5.place(x=50,y=290)
        self.b6=Label(self.k,text="Interstitial Implant\nExpertise in Conventional 2D & Clinical Planning\nExpertise in high precision Radiotherapy techniques",bg="white",fg="black",font=("arial",14))
        self.b6.place(x=50,y=330)
        self.b7=Label(self.k,text="Appointment",bg="white",fg="red",font=("arial",24))
        self.b7.place(x=50,y=450)
        self.b8=Label(self.k,text="MONDAY to FRIDAY\n10:00 AM to 5:00 PM",bg="white",fg="black",font=("arial",14))
        self.b8.place(x=50,y=490)
        self.b9=Label(self.k,text="Book an Appointment",bg="white",fg="red",font=("arial",24))
        self.b9.place(x=50,y=550)
        self.b11=Label(self.k,text="Time",bg="white",fg="black",font=("arial",18))
        self.b11.place(x=50,y=600)
        self.e11 = Entry(self.k,width=10,font=("arial",14))
        self.e11.place(x=150,y=600)
        self.b12=Label(self.k,text="Date",bg="white",fg="black",font=("arial",18))
        self.b12.place(x=290,y=600)
        self.e12 = Entry(self.k,width=10,font=("arial",14))
        self.e12.place(x=400,y=600)
        self.b13=Label(self.k,text="Day",bg="white",fg="black",font=("arial",18))
        self.b13.place(x=540,y=600)
        self.e13 = Entry(self.k,width=10,font=("arial",14))
        self.e13.place(x=630,y=600)
        self.b14=Label(self.k,text="Appointment No.",bg="white",fg="black",font=("arial",18))
        self.b14.place(x=50,y=660)
        self.e14 = Entry(self.k,width=10,font=("arial",18))
        self.e14.place(x=250,y=660)
        self.b15=Label(self.k,text="Username",bg="white",fg="black",font=("arial",18))
        self.b15.place(x=400,y=660)
        self.e15 = Entry(self.k,width=20,font=("arial",14))
        self.e15.place(x=550,y=660)

        self.b1= Button(text= "Submit",cursor="hand2" ,font=("cooper black",14, 'bold'),fg="red",bg="#0b1335",command=lambda:self.doc3_database())
        self.b1.place(x=330,y=710)

        self.b2=Button(text= "Back",cursor="hand2" ,font=("cooper black",14, 'bold'),fg="red",bg="#0b1335",command=lambda:self.doc())
        self.b2.place(x=490,y=710)

    def resultdoc3(self):
        self.doc3ano=self.e14.get()
        self.doc3uname=self.e15.get()
        self.doc3time=self.e11.get()
        self.doc3date=self.e12.get()
        self.doc3day=self.e13.get()
        return self.doc3ano,self.doc3uname,self.doc3time,self.doc3date,self.doc3day

    def doc3_database(self):
        self.creddoc3=self.resultdoc3()
        self.con=connect("appoint.db")
        self.cursor=self.con.cursor()
        try:
            self.cursor.execute("create table doc3_patient(Appointment_no integer primary key autoincrement ,Username varchar(50) not null,Time varchar(30) not null, Date varchar(40) not null,Day varchar(40) not null)")
        except:
            pass
        x=self.cursor.execute("select count(*) from doc3_patient where Appointment_no=%r and Day=%r"%(self.creddoc1[0],self.creddoc1[4]))
        #print(x)
        if list(x)[0][0]==0:
            if self.creddoc3[0]=="" or self.creddoc3[1]=="" or self.creddoc3[2]=="" or self.creddoc3[3]=="" or self.creddoc3[4]=="":
                messagebox.showinfo("Invalid","Empty Entry is not Allowed")
            else:
                self.cursor.execute("insert into doc3_patient values(%r,%r,%r,%r,%r)"%(self.creddoc3[0],self.creddoc3[1],self.creddoc3[2],self.creddoc3[3],self.creddoc3[4]))
                self.con.commit()
                messagebox.showinfo("Book","You have Successfully Booked your Appointment")
                self.k.destroy()
        else:
            messagebox.showinfo("Book","One of the credentials already exist \nEnter again")

    def doc4(self):
        self.k.destroy()
        self.k = Tk()
        self.k.geometry("900x800")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        self.k.config(bg="white")
        
        self.b1=Label(self.k,text="Dr.Shikha Mandloi",bg="white",fg="red",font=("arial",24))
        self.b1.place(x=50,y=100)
        self.b2=Label(self.k,text="Consultant Psychiatrist",bg="white",fg="black",font=("arial",14))
        self.b2.place(x=50,y=140)
        self.b3=Label(self.k,text="Professional summary",bg="white",fg="red",font=("arial",24))
        self.b3.place(x=50,y=190)
        self.b4=Label(self.k,text="2006 DPM DY Patil Vidhyapeeth,Pune,MH,India\n2002 MBBS Devi Ahilya Vishwavidyalaya,Indore,MP,India",bg="white",fg="black",font=("arial",14))
        self.b4.place(x=50,y=230)
        self.b5=Label(self.k,text="Technical Skills",bg="white",fg="red",font=("arial",24))
        self.b5.place(x=50,y=310)
        self.b6=Label(self.k,text="Child Psychiatry\nDe-addiction",bg="white",fg="black",font=("arial",14))
        self.b6.place(x=50,y=350)
        self.b7=Label(self.k,text="Appointment",bg="white",fg="red",font=("arial",24))
        self.b7.place(x=50,y=450)
        self.b8=Label(self.k,text="MONDAY to SATURDAY\n10:00 AM to 2:00 PM",bg="white",fg="black",font=("arial",14))
        self.b8.place(x=50,y=490)
        self.b9=Label(self.k,text="Book an Appointment",bg="white",fg="red",font=("arial",24))
        self.b9.place(x=50,y=550)
        self.b11=Label(self.k,text="Time",bg="white",fg="black",font=("arial",18))
        self.b11.place(x=50,y=600)
        self.e11 = Entry(self.k,width=10,font=("arial",14))
        self.e11.place(x=150,y=600)
        self.b12=Label(self.k,text="Date",bg="white",fg="black",font=("arial",18))
        self.b12.place(x=290,y=600)
        self.e12 = Entry(self.k,width=10,font=("arial",14))
        self.e12.place(x=400,y=600)
        self.b13=Label(self.k,text="Day",bg="white",fg="black",font=("arial",18))
        self.b13.place(x=540,y=600)
        self.e13 = Entry(self.k,width=10,font=("arial",14))
        self.e13.place(x=630,y=600)
        self.b14=Label(self.k,text="Appointment No.",bg="white",fg="black",font=("arial",18))
        self.b14.place(x=50,y=660)
        self.e14 = Entry(self.k,width=10,font=("arial",18))
        self.e14.place(x=250,y=660)
        self.b15=Label(self.k,text="Username",bg="white",fg="black",font=("arial",18))
        self.b15.place(x=400,y=660)
        self.e15 = Entry(self.k,width=20,font=("arial",14))
        self.e15.place(x=550,y=660)

        self.b1= Button(text= "Submit",cursor="hand2" ,font=("cooper black",14, 'bold'),fg="red",bg="#0b1335",command=lambda:self.doc4_database())
        self.b1.place(x=330,y=710)

        self.b2=Button(text= "Back",cursor="hand2" ,font=("cooper black",14, 'bold'),fg="red",bg="#0b1335",command=lambda:self.doc())
        self.b2.place(x=490,y=710)

    def resultdoc4(self):
        self.doc4ano=self.e14.get()
        self.doc4uname=self.e15.get()
        self.doc4time=self.e11.get()
        self.doc4date=self.e12.get()
        self.doc4day=self.e13.get()
        return self.doc4ano,self.doc4uname,self.doc4time,self.doc4date,self.doc4day


    def doc4_database(self):
        self.creddoc4=self.resultdoc4()
        self.con=connect("appoint.db")
        self.cursor=self.con.cursor()
        try:
            self.cursor.execute("create table doc4_patient(Appointment_no integer primary key autoincrement ,Username varchar(50) not null,Time varchar(30) not null, Date varchar(40) not null,Day varchar(40) not null)")
        except:
            pass
        x=self.cursor.execute("select count(*) from doc4_patient where Appointment_no=%r and Day=%r"%(self.creddoc4[0],self.creddoc4[4]))
        #print(x)
        if list(x)[0][0]==0:
            if self.creddoc4[0]=="" or self.creddoc4[1]=="" or self.creddoc4[2]=="" or self.creddoc4[3]=="" or self.creddoc4[4]=="":
                messagebox.showinfo("Invalid","Empty Entry is not Allowed")
            else:
                self.cursor.execute("insert into doc4_patient values(%r,%r,%r,%r,%r)"%(self.creddoc4[0],self.creddoc4[1],self.creddoc4[2],self.creddoc4[3],self.creddoc4[4]))
                self.con.commit()
                messagebox.showinfo("Book","You have Successfully Booked your Appointment")
                self.k.destroy()
        else:
            messagebox.showinfo("Book","One of the credentials already exist \nEnter again")
        

    def doc5(self):
        self.k.destroy()
        self.k = Tk()
        self.k.geometry("900x800")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        self.k.config(bg="white")
        
        self.b1=Label(self.k,text="Dr.Kamna Rathore",bg="white",fg="red",font=("arial",24))
        self.b1.place(x=50,y=100)
        self.b2=Label(self.k,text="Consultant Orthopedics",bg="white",fg="black",font=("arial",14))
        self.b2.place(x=50,y=140)
        self.b3=Label(self.k,text="Professional summary",bg="white",fg="red",font=("arial",24))
        self.b3.place(x=50,y=190)
        self.b4=Label(self.k,text="1975 D. Ortho College of Physicians & Surgeons,Mumbai,MH,India\n1972 MBBS Devi Ahilya Vishwavidyalaya,Indore,MP,India",bg="white",fg="black",font=("arial",14))
        self.b4.place(x=50,y=230)
        self.b5=Label(self.k,text="Technical Skills",bg="white",fg="red",font=("arial",24))
        self.b5.place(x=50,y=290)
        self.b6=Label(self.k,text="Arthroplasty\nSpine\nTrauma",bg="white",fg="black",font=("arial",14))
        self.b6.place(x=50,y=330)
        self.b7=Label(self.k,text="Appointment",bg="white",fg="red",font=("arial",24))
        self.b7.place(x=50,y=430)
        self.b8=Label(self.k,text="MONDAY(12:30 PM to 2:30 PM)\nWEDNESDAY(12:30 PM to 2:30 PM)\nFRIDAY(12:30 PM to 2:30 PM)\n",bg="white",fg="black",font=("arial",14))
        self.b8.place(x=50,y=470)
        self.b9=Label(self.k,text="Book an Appointment",bg="white",fg="red",font=("arial",24))
        self.b9.place(x=50,y=550)
        self.b11=Label(self.k,text="Time",bg="white",fg="black",font=("arial",18))
        self.b11.place(x=50,y=600)
        self.e11 = Entry(self.k,width=10,font=("arial",14))
        self.e11.place(x=150,y=600)
        self.b12=Label(self.k,text="Date",bg="white",fg="black",font=("arial",18))
        self.b12.place(x=290,y=600)
        self.e12 = Entry(self.k,width=10,font=("arial",14))
        self.e12.place(x=400,y=600)
        self.b13=Label(self.k,text="Day",bg="white",fg="black",font=("arial",18))
        self.b13.place(x=540,y=600)
        self.e13 = Entry(self.k,width=10,font=("arial",14))
        self.e13.place(x=630,y=600)
        self.b14=Label(self.k,text="Appointment No.",bg="white",fg="black",font=("arial",18))
        self.b14.place(x=50,y=660)
        self.e14 = Entry(self.k,width=10,font=("arial",18))
        self.e14.place(x=250,y=660)
        self.b15=Label(self.k,text="Username",bg="white",fg="black",font=("arial",18))
        self.b15.place(x=400,y=660)
        self.e15 = Entry(self.k,width=20,font=("arial",14))
        self.e15.place(x=550,y=660)

        self.b1= Button(text= "Submit",cursor="hand2" ,font=("cooper black",14, 'bold'),fg="red",bg="#0b1335",command=lambda:self.doc5_database())
        self.b1.place(x=330,y=710)

        self.b2=Button(text= "Back",cursor="hand2" ,font=("cooper black",14, 'bold'),fg="red",bg="#0b1335",command=lambda:self.doc())
        self.b2.place(x=490,y=710)

    def resultdoc5(self):
        self.doc5ano=self.e14.get()
        self.doc5uname=self.e15.get()
        self.doc5time=self.e11.get()
        self.doc5date=self.e12.get()
        self.doc5day=self.e13.get()
        return self.doc5ano,self.doc5uname,self.doc5time,self.doc5date,self.doc5day

    def doc5_database(self):
        self.creddoc5=self.resultdoc5()
        self.con=connect("appoint.db")
        self.cursor=self.con.cursor()
        try:
            self.cursor.execute("create table doc5_patient(Appointment_no integer primary key autoincrement ,Username varchar(50) not null,Time varchar(30) not null, Date varchar(40) not null,Day varchar(40) not null)")
        except:
            pass
        x=self.cursor.execute("select count(*) from doc5_patient where Appointment_no=%r and Day=%r"%(self.creddoc5[0],self.creddoc5[4]))
        #print(x)
        if list(x)[0][0]==0:
            if self.creddoc5[0]=="" or self.creddoc5[1]=="" or self.creddoc5[2]=="" or self.creddoc5[3]=="" or self.creddoc5[4]=="":
                messagebox.showinfo("Invalid","Empty Entry is not Allowed")
            else:
                self.cursor.execute("insert into doc5_patient values(%r,%r,%r,%r,%r)"%(self.creddoc5[0],self.creddoc5[1],self.creddoc5[2],self.creddoc5[3],self.creddoc5[4]))
                self.con.commit()
                messagebox.showinfo("Book","You have Successfully Booked your Appointment")
                self.k.destroy()
        else:
            messagebox.showinfo("Book","One of the credentials already exist \nEnter again")

    def doc6(self):
        self.k.destroy()
        self.k = Tk()
        self.k.geometry("900x800")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        self.k.config(bg="white")
        
        self.b1=Label(self.k,text="Dr. D. Panjwani",bg="white",fg="red",font=("arial",24))
        self.b1.place(x=50,y=100)
        self.b2=Label(self.k,text="Consultant Dermatologist",bg="white",fg="black",font=("arial",14))
        self.b2.place(x=50,y=140)
        self.b3=Label(self.k,text="Professional summary",bg="white",fg="red",font=("arial",24))
        self.b3.place(x=50,y=190)
        self.b4=Label(self.k,text="Dr.D.Panjwani has completed his M.B.B.S. from M G M Medical College, Indore in year\n2010 and her M.D. in Dermatology(DVL) in year 2015 from RIMS Govt.MC Ranchi.",bg="white",fg="black",font=("arial",14))
        self.b4.place(x=50,y=230)
        self.b7=Label(self.k,text="Appointment",bg="white",fg="red",font=("arial",24))
        self.b7.place(x=50,y=350)
        self.b8=Label(self.k,text="TUESDAY(10:00 AM to 4:00 PM)\nTHURSDAY(10:00 AM to 4:00 PM)\nFRIDAY(10:00 AM to 4:00 PM)\nSATURDAY(10:00 AM to 4:00 PM)\n",bg="white",fg="black",font=("arial",14))
        self.b8.place(x=50,y=390)
        self.b9=Label(self.k,text="Book an Appointment",bg="white",fg="red",font=("arial",24))
        self.b9.place(x=50,y=550)
        self.b11=Label(self.k,text="Time",bg="white",fg="black",font=("arial",18))
        self.b11.place(x=50,y=600)
        self.e11 = Entry(self.k,width=10,font=("arial",14))
        self.e11.place(x=150,y=600)
        self.b12=Label(self.k,text="Date",bg="white",fg="black",font=("arial",18))
        self.b12.place(x=290,y=600)
        self.e12 = Entry(self.k,width=10,font=("arial",14))
        self.e12.place(x=400,y=600)
        self.b13=Label(self.k,text="Day",bg="white",fg="black",font=("arial",18))
        self.b13.place(x=540,y=600)
        self.e13 = Entry(self.k,width=10,font=("arial",14))
        self.e13.place(x=630,y=600)
        self.b14=Label(self.k,text="Appointment No.",bg="white",fg="black",font=("arial",18))
        self.b14.place(x=50,y=660)
        self.e14 = Entry(self.k,width=10,font=("arial",18))
        self.e14.place(x=250,y=660)
        self.b15=Label(self.k,text="Username",bg="white",fg="black",font=("arial",18))
        self.b15.place(x=400,y=660)
        self.e15 = Entry(self.k,width=20,font=("arial",14))
        self.e15.place(x=550,y=660)

        self.b1= Button(text= "Submit",cursor="hand2" ,font=("cooper black",14, 'bold'),fg="red",bg="#0b1335",command=lambda:self.doc6_database())
        self.b1.place(x=330,y=710)

        self.b2=Button(text= "Back",cursor="hand2" ,font=("cooper black",14, 'bold'),fg="red",bg="#0b1335",command=lambda:self.doc())
        self.b2.place(x=490,y=710)

    def resultdoc6(self):
        self.doc6ano=self.e14.get()
        self.doc6uname=self.e15.get()
        self.doc6time=self.e11.get()
        self.doc6date=self.e12.get()
        self.doc6day=self.e13.get()
        return self.doc6ano,self.doc6uname,self.doc6time,self.doc6date,self.doc6day

    def doc6_database(self):
        self.creddoc6=self.resultdoc6()
        self.con=connect("appoint.db")
        self.cursor=self.con.cursor()
        try:
            self.cursor.execute("create table doc6_patient(Appointment_no integer primary key autoincrement ,Username varchar(50) not null,Time varchar(30) not null, Date varchar(40) not null,Day varchar(40) not null)")
        except:
            pass
        x=self.cursor.execute("select count(*) from doc6_patient where Appointment_no=%r and Day=%r"%(self.creddoc6[0],self.creddoc6[4]))
        #print(x)
        if list(x)[0][0]==0:
            if self.creddoc6[0]=="" or self.creddoc6[1]=="" or self.creddoc6[2]=="" or self.creddoc6[3]=="" or self.creddoc6[4]=="":
                messagebox.showinfo("Invalid","Empty Entry is not Allowed")
            else:
                self.cursor.execute("insert into doc6_patient values(%r,%r,%r,%r,%r)"%(self.creddoc6[0],self.creddoc6[1],self.creddoc6[2],self.creddoc6[3],self.creddoc6[4]))
                self.con.commit()
                messagebox.showinfo("Book","You have Successfully Booked your Appointment")
                self.k.destroy()
        else:
            messagebox.showinfo("Book","One of the credentials already exist \nEnter again")

    def dpage(self):
        self.k.destroy()
        self.k = Tk()
        self.k.geometry("700x600")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        #self.Bg2=PhotoImage(file="")
        #self.label = Label(self.frame1, image=)
        #self.label.place(x=0,y=0)
        self.k.config(bg="light yellow")
        self.button2=Button(text= "VIEW APPOINTMENTS", bd=5 ,font=("arial rounded mt",20, 'bold'),fg="red",bg="light blue",command=lambda:self.dloginn())
        self.button2.place(x=190,y=200)
        
        self.button4=Button(text= "HOME PAGE", bd=5 ,font=("arial rounded mt",20, 'bold'),fg="red",bg="light blue",command=lambda:self.main())
        self.button4.place(x=250,y=400)

    def dregister(self):
        self.k.destroy()
        self.k = Tk()
        self.k.geometry("1000x800")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        self.k.config(bg="brown")
        self.a=Label(self.k,text="Userame",bg="white",fg="blue",font=("arial",28))
        self.b=Label(self.k,text="Name",bg="white",fg="blue",font=("arial",28))
        self.c=Label(self.k,text="Mobile.No",bg="white",fg="blue",font=("arial",28))
        self.d=Label(self.k,text="Address",bg="white",fg="blue",font=("arial",28))
        self.e=Label(self.k,text="Age",bg="white",fg="blue",font=("arial",28))
        self.h=Label(self.k,text="Doctor Id",bg="white",fg="blue",font=("arial",28))
        
        self.a.place(x=80,y=100)
        self.b.place(x=80,y=200)
        self.c.place(x=80,y=300)
        self.d.place(x=80,y=400)
        self.e.place(x=80,y=500)
        self.h.place(x=80,y=600)
        self.e1=Entry(self.k,width=30,font=("arial",20))
        self.e2=Entry(self.k,width=30,font=("arial",20))
        self.e3=Entry(self.k,width=30,font=("arial",20))
        self.e4=Entry(self.k,width=30,font=("arial",20))
        self.e5=Entry(self.k,width=30,font=("arial",20))
        self.e6=Entry(self.k,width=30,font=("arial",20))

        self.e1.place(x=500,y=100)
        self.e2.place(x=500,y=200)
        self.e3.place(x=500,y=300)
        self.e4.place(x=500,y=400)
        self.e5.place(x=500,y=500)
        self.e6.place(x=500,y=600)

        self.button11=Button(text= "Submit",cursor="hand2" ,font=("cooper black",18, 'bold'),fg="red",bg="#0b1335",command=lambda:self.dreg_database())
        self.button11.place(x=500,y=700)

        self.button12=Button(text= "Back",cursor="hand2" ,font=("cooper black",18, 'bold'),fg="red",bg="#0b1335",command=lambda:self.dpage())
        self.button12.place(x=300,y=700)

    def dresultreg(self):
        self.dregdid=self.e6.get()
        self.dreguname=self.e1.get()
        self.dregname=self.e2.get()
        self.dregmob=self.e3.get()
        self.dregaddr=self.e4.get()
        self.dregage=self.e5.get()
        return self.dregdid,self.dreguname,self.dregname,self.dregmob,self.dregaddr,self.dregage

    def dreg_database(self):
        self.credreg=self.dresultreg()
        self.con=connect("appoint.db")
        self.cursor=self.con.cursor()
        try:
            self.cursor.execute("create table doctor1(Doctor_id integer primary key, Username varchar(50) not null,Name varchar(50) not null,Mob varchar(50) not null,Address varchar(100), Age varchar(5) not null)")
        except:
            pass
        x=self.cursor.execute("select count(*) from doctor1 where Username=%r and Username=%r"%(self.credreg[0],self.credreg[1]))
        #print(x)
        if list(x)[0][0]==0:
            if self.credreg[0]=="" or self.credreg[1]=="" or self.credreg[2]=="" or self.credreg[3]=="" or self.credreg[5]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed(except Address)")
            else:
                self.cursor.execute("insert into doctor1 values(%r,%r,%r,%r,%r,%r)"%(self.credreg[0],self.credreg[1],self.credreg[2],self.credreg[3],self.credreg[4],self.credreg[5]))
                self.con.commit()
                messagebox.showinfo("Register","You are Successfully Registered")
                self.dloginn()
        else:
            messagebox.showinfo("Register","Doctor Id or Username already Exist")

    def dloginn(self):
        self.k.destroy()
        self.k = Tk()
        self.k.geometry("1000x700")
        self.k.title("KM HOSPITAL")
        self.k.iconbitmap('logo.ico')
        self.l_title = Message(text="KM HOSPITAL",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        self.l_title.config(font=("Courier","50","bold"))
        self.l_title.pack(side="top")
        self.k.config(bg="brown")
        self.a1=Label(self.k,text="UserName",bg="white",fg="blue",font=("arial",28))
        self.b1=Label(self.k,text="Name",bg="white",fg="blue",font=("arial",28))
        self.c1=Label(self.k,text="Doctor Id",bg="white",fg="blue",font=("arial",28))

        self.a1.place(x=80,y=150)
        self.b1.place(x=80,y=250)
        self.c1.place(x=80,y=350)


        self.e7=Entry(self.k,width=30,font=("arial",20))
        self.e8=Entry(self.k,width=30,font=("arial",20))
        self.e9=Entry(self.k,width=30,font=("arial",20))

        self.e7.place(x=500,y=150)
        self.e8.place(x=500,y=250)
        self.e9.place(x=500,y=350)

        self.button13=Button(text= "Register",cursor="hand2" ,font=("cooper black",18, 'bold'),fg="red",bg="#0b1335",command=lambda:self.dregister())
        self.button13.place(x=350,y=600)

        self.button13=Button(text= "Submit",cursor="hand2" ,font=("cooper black",18, 'bold'),fg="red",bg="#0b1335",command=lambda:self.dlog_database())
        self.button13.place(x=450,y=500)

        self.button11=Button(text= "Back",cursor="hand2" ,font=("cooper black",18, 'bold'),fg="red",bg="#0b1335",command=lambda:self.dpage())
        self.button11.place(x=550,y=600)


    def resultdlog(self):
        self.dloguname=self.e7.get()
        self.dlogname=self.e8.get()
        self.dlogdid=self.e9.get()
        return self.dlogdid,self.dloguname,self.dlogname

    def dlog_database(self):
        self.creddlog=self.resultdlog()
        self.con=connect("appoint.db")
        self.cursor=self.con.cursor()
        try:
            self.cursor.execute("create table doctor1(Doctor_id integer primary key, Username varchar(50) not null,Name varchar(50) not null,Mob varchar(50) not null,Address varchar(100), Age varchar(5) not null)")
        except:
            pass
        x=self.cursor.execute("select count(*) from doctor1 where Doctor_id=%r and Username=%r and Name=%r"%(self.creddlog[0],self.creddlog[1],self.creddlog[2]))
        if list(x)[0][0]==0:
            if self.creddlog[0]=="" or self.creddlog[1]=="" or self.creddlog[2]=="":
                messagebox.showinfo("Login","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Login","You are Not Registered Yet")
            
        else:
            messagebox.showinfo("Login","You have Successfully Log In")            
            self.doc1page()
        
        
    def doc1page(self):
        pass

    
        
        
r=Km()
r.main()
        
    
