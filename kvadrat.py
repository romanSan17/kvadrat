import numpy as np
import matplotlib.pyplot as plt
from ctypes import c_bool, c_buffer, c_byte, c_char
from tkinter import *
from math import sqrt

def calculate():
    a_=float(a.get())
    b_=float(b.get())
    c_=float(c.get())
    D=b_*b_-4*a_*c_ 
    if D>0:
        x1_=round((-1*b_+sqrt(D))/(2*a_),2)
        x2_=round((-1*b_-sqrt(D))/(2*a_),2)
        t=f"X1={x1_}, \nX2={x2_}"
        graf=True 
    elif D==0:
        x1_=round((-1*b_)/(2*a_),2)
        t=f"X1={x1_}" 
        graf=True
    else:
        t="нет корней"
        graf=False 
    vastus.configure(text=f"D={D}\n{t}")
    a.configure(bg="lightblue")
    b.configure(bg="lightblue")
    c.configure(bg="lightblue")
    graafik(graf, D)

def graafik(graf:bool,D: float):
    if graf==True:
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0**2+b_*x0+c_ 
        x1=np.arange(x0-10, x0+10, 0.5)
        y1=a_*x1**2+b_*x1+c_ 
        fig=plt.figure()
        plt.plot(x1, y1,'r-d')
        plt.title('kvadratnoe uravnenije')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"vershina"
    else:
        text=f"график не построить"
    vastus.configure(text=f"D={D}\n{text}")
aken = Tk()
aken.geometry("720x600")
aken.title("Tkinteri kasutamine")

tekst = "Kvadraatilise võrrandi lahendamine"
tekst1 = "x**2+"
tekst2 = "x+"
tekst3 = "=0"
pealkiri = Label(aken, 
                 text=tekst, 
                 bg="#ffffff", 
                 fg="#668F25", 
                 font="Algeria 20", 
                 height=3, 
                 width=len(tekst),
                 cursor="man")
x2 = Label(aken, 
           text=tekst1, 
           bg="#ffffff", 
           fg="#668F25", 
           font="Algeria 20", 
           height=1,
           width=5,
           cursor="man")
x22 = Label(aken, 
            text=tekst2, 
            bg="#ffffff", 
            fg="#668F25", 
            font="Algeria 20", 
            height=1, 
            width=5,
            cursor="man")
x222 = Label(aken, 
            text=tekst3, 
            bg="#ffffff", 
            fg="#668F25", 
            font="Algeria 20", 
            height=1, 
            width=5,
            cursor="man")
a = Entry(aken,
                bg="#C6E2FF",
                fg="#668F25",
                font="Algeria 20", 
                width=5,
                justify=LEFT)
b = Entry(aken, 
                bg="#C6E2FF",
                fg="#668F25",
                font="Algeria 20", 
                width=5)
c = Entry(aken,
                bg="#C6E2FF",
                fg="#668F25",
                font="Algeria 20", 
                width=5)


nupp = Button(aken,
              text="vastus!",
              font="Arial 20",
              height=3, 
              width=len(tekst),
              relief=RAISED,
              command=calculate)

vastus = Label(aken, 
               text="", 
               bg="#ffffff", 
               fg="#668F25", 
               font="Arial 14", 
               height=4, 
               width=25,
               cursor="man")

pealkiri.grid(row=0, column=0, columnspan=6) 

nupp.grid(row=3, column=0, columnspan=6)

a.grid(row=2, column=0)
x2.grid(row=2, column=1)
b.grid(row=2, column=2)
x22.grid(row=2, column=3)
c.grid(row=2, column=4)
x222.grid(row=2, column=5)

vastus.grid(row=4, column=0, columnspan=6)

aken.mainloop()




































#from tkinter import *
#from tkinter import messagebox as mb
#k=0
#def valjuta():
#    global k
#    k+=1
#    nupp.configure(text=k)
#def valjuta_(event):
#    global k
#    k-=1
#    nupp.configure(text=k)
#def tst_psse(event):
#    t=textbox.get()
#    if t=="":
#        mb.showwarning("Tähelepanu!","On vaja sisestada numbreid!")
#    else:
#        pealkiri.configure(text=t,widht=len(t))
#        textbox.delete(0,END)
#        mb.showinfo("Aruanne","Tekst oli lisatud pealkijasse!")
#def valik():
#    arv=var.get()
#    textbox.insert(0,arv)
#aken=Tk()
#aken.geometry("400x600")
#aken.iconbitmap('icon.ico')
#aken.title("Tkinteri kasutamine")
#tekst="Pealkiri"
#pealkiri=Label(aken, 
#               text=tekst, 
#               bg="#C6E2FF", 
#               fg="#668F25", 
#               font="Algeria 20", 
#               height=3, width=len(tekst),
#               cursor="man")
#textbox=Entry(aken,
#             bg="#C6E2FF",
#             fg="#668F25",
#             font="Algeria 20", 
#             width=20,
#             justify=CENTER ) #show="*"
#nupp=Button(aken,
#            text="Vajuta mind!",
#            font="Arial 20",
#            height=3, width=len(tekst),
#            relief=RAISED,
#            command=valjuta()) #SUNKEN, GROOVE
#f=Frame(aken)
#var=IntVar() #StringVar
#e=Radiobutton(f,text="Esimine",variable=var,value=1,font="Arial 20",command=valik)
#t=Radiobutton(f,text="Teine",variable=var,value=2,font="Arial 20",command=valik)
#k_=Radiobutton(f,text="Kolmas",variable=var,value=3,font="Arial 20",command=valik)
#nupp.bind("<Button-3>", valjuta_) #PKM
#textbox.bind("<Return>",tst_psse) #SUNKEN, GROOVE

#obj=[pealkiri,textbox,nupp,f]
#for i in obj:
#    i.pack()
#obj2=[e,t,k_]
#for i in range(len(obj2)):
#    obj2[i].grid(row=0,column=1)
#aken.mainloop()