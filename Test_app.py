from tkinter import *
from PIL import Image,ImageTk
import time
#root window 
welcomewin = Tk()
welcomewin.title("Welcome to Exthand")
welcomewin.configure(background='#3C3C3C')
logo = Image.open("D:\Exthand\Title.png")
logocard = ImageTk.PhotoImage(logo)
logolabel = Label(image=logocard)
logolabel.image = logocard
logolabel.place(x=3, y=20)
welcome = Label(welcomewin,text='Welcome to \n\tExtHand',font="Helvetica 10 bold italic")
f1bg = '#ab47bc'
frame1 = LabelFrame(welcomewin,text="Begin Now.....\n\n",background=f1bg,borderwidth=0,highlightthickness=0,)
frame1.grid(column=0,row=6,padx=20,pady=30)

header = Label(welcomewin,background='#3C3C3C',image=PhotoImage('Title.png'))


#Holders for frame1
name=StringVar()
mail=StringVar()
phone = StringVar()

#frame1 widgets
namelbl  = Label(frame1,background=f1bg,foreground='#FAFAFA',text="Please Enter Your Name :")
namelbl.grid(row=1,sticky=W,padx=0)
nameentry = Entry(frame1,width=20,textvariable=name)
nameentry.grid(row=1,column=2,sticky=W,padx=0)
emaillbl = Label(frame1,background=f1bg,foreground='#FAFAFA',text="E-Mail                :")
emaillbl.grid(row=2,sticky=W,padx=10)
mailentry = Entry(frame1,width=20,textvariable=mail)
mailentry.grid(row=2,column=2,sticky=W,padx=10)
phonelbl = Label(frame1,background=f1bg,foreground='#FAFAFA',text="Phone Number :")
phonelbl.grid(row=3,sticky=W,padx=20)
phoneentry = Entry(frame1,width=20,textvariable=phone)
phoneentry.grid(column=2,row=3,sticky=W,padx=20)

#frame1 button functions 
def pwgotp():
    submit.configure(text="Please Wait...",foreground='#FAFAFA',background='lightgreen')
    check()
def enter():
    submit.configure(text="Getting OTP",foreground='#FAFAFA',background='lightgreen',command=pwgotp)

#get OTP (frame1)
submit = Button(frame1,text="Get OTP",foreground='#FAFAFA',background="lightgreen",command=enter)
submit.grid(row=5,sticky=W)
welcomewin.mainloop()
