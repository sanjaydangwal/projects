import tkinter as tk
# from tkinter import ttk
from tkinter import messagebox as m_box
win = tk.Tk()
win.title("Tic Tac Toe")
cantainer = tk.LabelFrame(win)
win.geometry("370x280")
win.resizable(0,0)
c=1
def clear():
    b1['text'] = ""
    b2['text'] = ""
    b3['text'] = ""
    b4['text'] = ""
    b5['text'] = ""
    b6['text'] = ""
    b7['text'] = ""
    b8['text'] = ""
    b9['text'] = ""
def show(b):
    global c
    if b['text'] =="":
        c+=1
        if c%2==0:
            b['text'] = 'X'
        else:
            b['text'] = 'O'
        if b1['text']=='X' and b2['text']=='X' and b3['text']=='X':
            m_box.showinfo("WINNER","PLAYER ONE WIN!")
            clear()
        elif b1['text']=='O' and b2['text']=='O' and b3['text']=='O':
            m_box.showinfo("WINNER","PLAYER TWO WIN!")
            clear()
        elif b4['text']=='X' and b5['text']=='X' and b6['text']=='X':
            m_box.showinfo("WINNER","PLAYER ONE WIN!")
            clear()
        elif b4['text']=='O' and b5['text']=='O' and b6['text']=='O':
            m_box.showinfo("WINNER","PLAYER TWO WIN!")
            clear()
        elif b7['text']=='X' and b8['text']=='X' and b9['text']=='X':
            m_box.showinfo("WINNER","PLAYER ONE WIN!")
            clear()
        elif b7['text']=='O' and b8['text']=='O' and b9['text']=='O':
            m_box.showinfo("WINNER","PLAYER TWO WIN!")
            clear()
        elif b1['text']=='X' and b5['text']=='X' and b9['text']=='X':
            m_box.showinfo("WINNER","PLAYER ONE WIN!")
            clear()
        elif b1['text']=='O' and b5['text']=='O' and b9['text']=='O':
            m_box.showinfo("WINNER","PLAYER TWO WIN!")
            clear()
        elif b3['text']=='X' and b5['text']=='X' and b7['text']=='X':
            m_box.showinfo("WINNER","PLAYER ONE WIN!")
            clear()
        elif b3['text']=='O' and b5['text']=='O' and b7['text']=='O':
            m_box.showinfo("WINNER","PLAYER TWO WIN!")
            clear()
        elif b1['text']=='X' and b4['text']=='X' and b7['text']=='X':
            m_box.showinfo("WINNER","PLAYER ONE WIN!")
            clear()
        elif b1['text']=='O' and b4['text']=='O' and b7['text']=='O':
            m_box.showinfo("WINNER","PLAYER TWO WIN!")
            clear()
        elif b2['text']=='X' and b5['text']=='X' and b8['text']=='X':
            m_box.showinfo("WINNER","PLAYER ONE WIN!")
            clear()
        elif b2['text']=='O' and b5['text']=='O' and b8['text']=='O':
            m_box.showinfo("WINNER","PLAYER TWO WIN!")
            clear()
        elif b3['text']=='X' and b6['text']=='X' and b9['text']=='X':
            m_box.showinfo("WINNER","PLAYER ONE WIN!")
            clear()
        elif b3['text']=='O' and b6['text']=='O' and b9['text']=='O':
            m_box.showinfo("WINNER","PLAYER TWO WIN!")
            clear()
        
        if b1['text']!="" and b2['text']!="" and b3['text']!="" and b4['text']!="" and b5['text']!="" and b6['text']!="" and b7['text']!="" and b8['text']!="" and b9['text']!="":
            m_box.showwarning("OVER","GAME OVER")
            clear()

# -------row 1-----------

b1= tk.Button(cantainer,width = 15,height = 5,command = lambda : show(b1))
b1.grid(row=0,column=0)

b2= tk.Button(cantainer,width = 15,height = 5,command = lambda : show(b2))
b2.grid(row=0,column=1)

b3= tk.Button(cantainer,width = 15,height = 5,command = lambda : show(b3))
b3.grid(row=0,column=2)

# -------row 2-----------


b4= tk.Button(cantainer,width = 15,height = 5,command = lambda : show(b4))
b4.grid(row=1,column=0)

b5= tk.Button(cantainer,width = 15,height = 5,command = lambda : show(b5))
b5.grid(row=1,column=1)

b6= tk.Button(cantainer,width = 15,height = 5,command = lambda : show(b6))
b6.grid(row=1,column=2)


# -------row 3-----------

b7= tk.Button(cantainer,width = 15,height = 5,command = lambda : show(b7))
b7.grid(row=2,column=0)

b8= tk.Button(cantainer,width = 15,height = 5,command = lambda : show(b8))
b8.grid(row=2,column=1)

b9= tk.Button(cantainer,width = 15,height = 5,command = lambda : show(b9))
b9.grid(row=2,column=2)



cantainer.grid(row = 0 ,column = 0,padx = 10,pady = 10)
win.mainloop()
