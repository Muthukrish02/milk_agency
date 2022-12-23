import db
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
d=db.DatabaseM("milky.db")

def clicku(event):  # fun_for_tk
    en_u.config(state=NORMAL)
    en_u.delete(0, END)


def clickp(event):
    en_p.config(state=NORMAL, show="*")
    en_p.delete(0, END)


def uget():
    ud = en_u.get()
    pd=en_p.get()
    r=[(ud,)]
    s=[(pd,)]
    c=d.check_u(r)
    b=d.check_p(s)
    if c and b==True:
        messagebox.showinfo("message","loin sussusfully")
    else:
        messagebox.showerror("message","user_id or password wrong")
    en_u.delete(0,END)
    en_p.delete(0, END)





k = Tk()

k.title("milk shop")
k.geometry("925x500+300+200")
k.config(bg="#fdd6ff")
#k.iconbitmap(file="ico.ico")
fo = Font(family="DejaVu Sans Extralight", size=30, weight="normal",)
frame1=Frame(k,width=350,height=390,bg='white')
frame1.place(x=480,y=50)
img=PhotoImage(file="PinClipart.com_clip-art-yogurt_2009449.png")
Label(k,image=img,border=0,bg='#fdd6ff').place(x=60,y=80)
# Label
l = Label(frame1, text="Milk Agency", font=fo, bg="white", fg="#57a1f8")
l.pack()
l.place(x=50, y=5)
fo_= Font(family="DejaVu Sans Extralight", size=20, weight="normal",)
Label(frame1,text='Login',font=fo_,bg="white",fg="#f75e5e").place(x=10,y=70)
# Entry_user
Efnt = Font(family="times", size=15, weight="normal", )
en_u = Entry(frame1,width=25, font=Efnt, bg="white",border=0)
en_u.insert(0, "user name", )
en_u.place(x=30, y=150)
Frame(frame1,width=295,height=2,bg='black').place(x=25,y=175)
#en_u.config(state=DISABLED)
en_u.bind("<Button-1>", clicku)
# Entry_password
en_p = Entry(frame1,width=25,font=Efnt, bg="white",border=0)
en_p.pack()
en_p.place(x=30, y=200)
en_p.insert(0, " password")
Frame(frame1,width=295,height=2,bg='black').place(x=25,y=225)
#en_p.config(state=DISABLED)
en_p.bind("<Button-1>", clickp)
# button
pic=PhotoImage(file="images.png")
but = Button(frame1,width=15,pady=7,text="Login", command=uget,fg="#57a1f8",bg="white",border=0)
but.pack()
but.place(x=95, y=280)



labe=Button(frame1,text="register here",border=0,bg='white',cursor='hand2',fg='#57a1f8',command=uget)
labe.place(x=20,y=340)
k.mainloop()

