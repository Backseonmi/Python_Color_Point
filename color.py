from tkinter import*
from PIL import ImageTk, Image
root = Tk()

root.title("Color Point")
root.fullScreenState = False
root.attributes('-fullscreen', root.fullScreenState)
root.w, root.h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d" % (root.w, root.h))
root.resizable(False,False)
root.configure(bg = 'pink')


label = Label(root, text="Color Point", font = ("Arial",24), fg ="#00BFFF", bg = 'pink', anchor = SE).pack()

def open_window1():
    global images
    top = Toplevel()
    top.title("색 정보")
    top.fullScreenState = False
    top.attributes('-fullscreen', top.fullScreenState)
    top.w, top.h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d" % (top.w, top.h))
    top.resizable(False,False)
    label1 = Label(top, text="2010년도의 색").pack()
    images = ImageTk.PhotoImage(Image.open('image/img_2010.jpg'))
    Label(top, image=images).pack()
    Button(top, text="닫기", command=top.destroy).pack(pady=10)

def open_window2():
    global images
    top = Toplevel()
    top.title("색 정보")
    top.fullScreenState = False
    top.attributes('-fullscreen', top.fullScreenState)
    top.w, top.h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d" % (top.w, top.h))
    top.resizable(False,False)
    label1 = Label(top, text="2011년도의 색").pack()
    images = ImageTk.PhotoImage(Image.open('image/img_2011.jpg'))
    Label(top, image=images).pack()
    Button(top, text="닫기", command=top.destroy).pack(pady=10)

def open_window3():
    global images
    top = Toplevel()
    top.title("색 정보")
    top.fullScreenState = False
    top.attributes('-fullscreen', top.fullScreenState)
    top.w, top.h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d" % (top.w, top.h))
    top.resizable(False,False)
    label1 = Label(top, text="2012년도의 색").pack()
    images = ImageTk.PhotoImage(Image.open('image/img_2012.jpg'))
    Label(top, image=images).pack()
    Button(top, text="닫기", command=top.destroy).pack(pady=10)

def open_window4():
    global images
    top = Toplevel()
    top.title("색 정보")
    top.fullScreenState = False
    top.attributes('-fullscreen', top.fullScreenState)
    top.w, top.h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d" % (top.w, top.h))
    top.resizable(False,False)
    label1 = Label(top, text="2013년도의 색").pack()
    images = ImageTk.PhotoImage(Image.open('image/img_2013.jpg'))
    Label(top, image=images).pack()
    Button(top, text="닫기", command=top.destroy).pack(pady=10)

def open_window5():
    global images
    top = Toplevel()
    top.title("색 정보")
    top.fullScreenState = False
    top.attributes('-fullscreen', top.fullScreenState)
    top.w, top.h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d" % (top.w, top.h))
    top.resizable(False,False)
    label1 = Label(top, text="2014년도의 색").pack()
    images = ImageTk.PhotoImage(Image.open('image/img_2014.jpg'))
    Label(top, image=images).pack()
    Button(top, text="닫기", command=top.destroy).pack(pady=10)

def open_window6():
    global images
    top = Toplevel()
    top.title("색 정보")
    top.fullScreenState = False
    top.attributes('-fullscreen', top.fullScreenState)
    top.w, top.h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d" % (top.w, top.h))
    top.resizable(False,False)
    label1 = Label(top, text="2015년도의 색").pack()
    images = ImageTk.PhotoImage(Image.open('image/img_2015.jpg'))
    Label(top, image=images).pack()
    Button(top, text="닫기", command=top.destroy).pack(pady=10)

def open_window7():
    global images
    top = Toplevel()
    top.title("색 정보")
    top.fullScreenState = False
    top.attributes('-fullscreen', top.fullScreenState)
    top.w, top.h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d" % (top.w, top.h))
    top.resizable(False,False)
    label1 = Label(top, text="2016년도의 색").pack()
    images = ImageTk.PhotoImage(Image.open('image/img_2016.jpg'))
    Label(top, image=images).pack()
    Button(top, text="닫기", command=top.destroy).pack(pady=10)

def open_window8():
    global images
    top = Toplevel()
    top.title("색 정보")
    top.fullScreenState = False
    top.attributes('-fullscreen', top.fullScreenState)
    top.w, top.h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d" % (top.w, top.h))
    top.resizable(False,False)
    label1 = Label(top, text="2017년도의 색").pack()
    images = ImageTk.PhotoImage(Image.open('image/img_2017.jpg'))
    Label(top, image=images).pack()
    Button(top, text="닫기", command=top.destroy).pack(pady=10)

def open_window9():
    global images
    top = Toplevel()
    top.title("색 정보")
    top.fullScreenState = False
    top.attributes('-fullscreen', top.fullScreenState)
    top.w, top.h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d" % (top.w, top.h))
    top.resizable(False,False)
    label1 = Label(top, text="2018년도의 색").pack()
    images = ImageTk.PhotoImage(Image.open('image/img_2018.jpg'))
    Label(top, image=images).pack()
    Button(top, text="닫기", command=top.destroy).pack(pady=10)

def open_window10():
    global images
    top = Toplevel()
    top.title("색 정보")
    top.fullScreenState = False
    top.attributes('-fullscreen', top.fullScreenState)
    top.w, top.h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d" % (top.w, top.h))
    top.resizable(False,False)
    label1 = Label(top, text="2019년도의 색").pack()
    images = ImageTk.PhotoImage(Image.open('image/img_2019.jpg'))
    Label(top, image=images).pack()
    Button(top, text="닫기", command=top.destroy).pack(pady=10)

def open_window11():
    global images
    top = Toplevel()
    top.title("색 정보")
    top.fullScreenState = False
    top.attributes('-fullscreen', top.fullScreenState)
    top.w, top.h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d" % (top.w, top.h))
    top.resizable(False,False)
    label1 = Label(top, text="2020년도의 색").pack()
    images = ImageTk.PhotoImage(Image.open('image/img_2020.jpg'))
    Label(top, image=images).pack()
    Button(top, text="닫기", command=top.destroy).pack(pady=10)

def open_window12():
    global images
    top = Toplevel()
    top.title("색 정보")
    top.fullScreenState = False
    top.attributes('-fullscreen', top.fullScreenState)
    top.w, top.h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d" % (top.w, top.h))
    top.resizable(False,False)
    label1 = Label(top, text="2021년도의 색").pack()
    images = ImageTk.PhotoImage(Image.open('image/img_2021.jpg'))
    Label(top, image=images).pack()
    Button(top, text="닫기", command=top.destroy).pack(pady=10)

def open_window13():
    global images
    top = Toplevel()
    top.title("색 정보")
    top.fullScreenState = False
    top.attributes('-fullscreen', top.fullScreenState)
    top.w, top.h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d" % (top.w, top.h))
    top.resizable(False,False)
    label1 = Label(top, text="2022년도의 색").pack()
    images = ImageTk.PhotoImage(Image.open('image/img_2022.jpg'))
    Label(top, image=images).pack()
    Button(top, text="닫기", command=top.destroy).pack(pady=10)

b1 = Button(root, text = '2010', command=open_window1)
b1.pack(pady=8)
b2 = Button(root, text = '2011', command=open_window2)
b2.pack(pady=8)
b3 = Button(root, text = '2012', command=open_window3)
b3.pack(pady=8)
b4 = Button(root, text = '2013', command=open_window4)
b4.pack(pady=8)
b5 = Button(root, text = '2014', command=open_window5)
b5.pack(pady=8)
b6 = Button(root, text = '2015', command=open_window6)
b6.pack(pady=8)
b7 = Button(root, text = '2016', command=open_window7)
b7.pack(pady=8)
b8 = Button(root, text = '2017', command=open_window8)
b8.pack(pady=8)
b9 = Button(root, text = '2018', command=open_window9)
b9.pack(pady=8)
b10 = Button(root, text = '2019', command=open_window10)
b10.pack(pady=8)
b11 = Button(root, text = '2020', command=open_window11)
b11.pack(pady=8)
b12 = Button(root, text = '2021', command=open_window12)
b12.pack(pady=8)
b13 = Button(root, text = '2022', command=open_window13)
b13.pack(pady=8)


mainloop()

        


    


# Button(ws, text="Subscribe", command=subscribe).pack(pady=20)

# st = Style()
# st.configure('W.TButton', background='#345', foreground='black', font=('Arial', 14 ))
# Button(ws, text="Click", command=None).pack()

# Button(ws, text='Smash Me', style='W.TButton', command=None).pack()
# Button(ws,text="Click",command=None).grid(row=0, column=0)
# Button(ws, text="Click", command=None).place(x=20, y=20)
# Button(ws, text='Smash Me!', height=10, width=20).pack(pady=10)
# Button(ws, text='Smash Me!', height=10, width=20, bg='#567', fg='White').pack(pady=10)

# dwnd = PhotoImage(file='download.png')
# Button(ws, image=dwnd, command=None, borderwidth = 0).pack(pady=10)

# Button(ws, text="Smash Me", activebackground='#345',activeforeground='white', padx=5, pady=5 ).pack(pady=10)

# Button(ws, text="Click", bg="blue", fg="#000").pack()

# Button(ws, text="font", font=('arial bold', 18)).pack()
