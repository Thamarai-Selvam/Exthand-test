from tkinter import *
Intro = Tk()
Intro.title('Introduction')
Intro.configure(bg='#3c3c3c')
Intro.geometry('700x500+0+0')
Introtext = Label(Intro,text='Welcome',font='Montserrat 30 bold italic',bg='#3c3c3c',fg='blue')
Introtext.grid(sticky=W+E+N+S,pady=5)
Intrologo = Label(Intro,text='This Is ExtHand For You',font='Montserrat 30 bold italic',bg='#3c3c3c',fg='lightgreen')
Intrologo.grid(sticky=E+N+S,pady=5)
