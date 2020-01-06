import tkinter as tk
from tkinter import ttk
main = tk.Tk()
main.title("Calculator")
main.geometry("250x350+300+300")
main.resizable(0,0)

display_var = tk.StringVar()

display = tk.Frame(main,bg = "#ffffff")
display.pack(expand = True,fill = "both")

frame1 = tk.Frame(main)
frame1.pack(expand = True,fill = "both")

frame2 = tk.Frame(main)
frame2.pack(expand = True,fill = "both")

frame3 = tk.Frame(main)
frame3.pack(expand = True,fill = "both")

frame4 = tk.Frame(main)
frame4.pack(expand = True,fill = "both")

frame5 = tk.Frame(main)
frame5.pack(expand = True,fill = "both")


#display
display_screen = tk.Label(display,background = "#ffffff",font = ("verdana",20),textvariable = display_var)
display_screen.pack(side = "right")
display_var.set("0")

# number press function
def numPress(num):
    if display_var.get()=="0":
        display_var.set("")
    elif display_var.get()[-1] in ('+','-','x','%','/') and num == ".":
        display_var.set(display_var.get()+'0')
    display_var.set(display_var.get()+num)

# operator press function
def optPress(opt):
    if display_var.get()[-1] not in ('-','+','/','%','x'):
        display_var.set(display_var.get()+opt)

#for result button
def result():
    expration = display_var.get()
    
    try:
        display_var.set(eval(expration.replace("x","*")))
    except ZeroDivisionError :
        display_var.set("undefined")
    if len(display_var.get()) > 14:
        display_var.set(display_var.get()[0:14])

#for clear button
def clear():
    display_var.set("0")        

#for backspace button
def back():
    var = display_var.get()[0:len(display_var.get())-1]
    display_var.set(var)
    if display_var.get() == "":
        display_var.set("0")

#for squar function
def sqr():
    try:
        display_var.set(int(display_var.get())**2)
    except ValueError:
        i =''
        ch = display_var.get()
        var = ch[::-1]
        for j in var:
            if j in ('+','-','x','%','/'):
                break
            else:
                i +=j
                ch = ch[0:len(ch)-1]
        i = int(i)**2
        display_var.set(ch+str(i))
    if len(display_var.get())>14:
        display_var.set(display_var.get()[0:14])

#for dot button
def dotPress():
    i = ''
    ch = display_var.get()
    var = ch[::-1]
    for j in var:
        if j in ('-','+','/','%','x'):
            break
        else:
            i+=j
    if '.' not in i:
        display_var.set(display_var.get()+'.')


#first row
btnSqr = tk.Button(frame1,text = "x\u00b2",font = ("verdana",21),relief = "groove",border = 0,command = sqr)
btnSqr.pack(side = "left",expand = True,fill = "both")

btnMod = tk.Button(frame1,text = "%",font = ("verdana",21),relief = "groove",border = 0,command = lambda : optPress('%'))
btnMod.pack(side = "left",expand = True,fill = "both")

btnBack = tk.Button(frame1,text = "<-",font = ("verdana",21),relief = "groove",border = 0,command = back)
btnBack.pack(side = "left",expand = True,fill = "both")

btnDiv = tk.Button(frame1,text = "/",font = ("verdana",21),relief = "groove",border = 0,command = lambda : optPress('/'))
btnDiv.pack(side = "left",expand = True,fill = "both")

#second row
btn7 = tk.Button(frame2,text = "7",font = ("verdana",21),relief = "groove",border = 0,command = lambda : numPress('7'))
btn7.pack(side = "left",expand = True,fill = "both")

btn8 = tk.Button(frame2,text = "8",font = ("verdana",21),relief = "groove",border = 0,command = lambda : numPress('8'))
btn8.pack(side = "left",expand = True,fill = "both")

btn9 = tk.Button(frame2,text = "9",font = ("verdana",21),relief = "groove",border = 0,command = lambda : numPress('9'))
btn9.pack(side = "left",expand = True,fill = "both")

btnMul = tk.Button(frame2,text = " x",font = ("verdana",21),relief = "groove",border = 0,command = lambda : optPress('x'))
btnMul.pack(side = "left",expand = True,fill = "both")

#third row
btn4 = tk.Button(frame3,text = "4",font = ("verdana",21),relief = "groove",border = 0,command = lambda : numPress('4'))
btn4.pack(side = "left",expand = True,fill = "both")

btn5 = tk.Button(frame3,text = "5",font = ("verdana",21),relief = "groove",border = 0,command = lambda : numPress('5'))
btn5.pack(side = "left",expand = True,fill = "both")

btn6 = tk.Button(frame3,text = "6",font = ("verdana",21),relief = "groove",border = 0,command = lambda : numPress('6'))
btn6.pack(side = "left",expand = True,fill = "both")

btnMinus = tk.Button(frame3,text = " -",font = ("verdana",21),relief = "groove",border = 0,command = lambda : optPress('-'))
btnMinus.pack(side = "left",expand = True,fill = "both")

#fourth row
btn1 = tk.Button(frame4,text = "1",font = ("verdana",21),relief = "groove",border = 0,command = lambda : numPress('1'))
btn1.pack(side = "left",expand = True,fill = "both")

btn2 = tk.Button(frame4,text = "2",font = ("verdana",21),relief = "groove",border = 0,command = lambda : numPress('2'))
btn2.pack(side = "left",expand = True,fill = "both")

btn3 = tk.Button(frame4,text = "3",font = ("verdana",21),relief = "groove",border = 0,command = lambda : numPress('3'))
btn3.pack(side = "left",expand = True,fill = "both")

btnPlus = tk.Button(frame4,text = "+",font = ("verdana",21),relief = "groove",border = 0,command = lambda : optPress('+'))
btnPlus.pack(side = "left",expand = True,fill = "both")

#fifth row
btnClear = tk.Button(frame5,text = "c",font = ("verdana",21),relief = "groove",border = 0,command = clear)
btnClear.pack(side = "left",expand = True,fill = "both")

btn0 = tk.Button(frame5,text = "0",font = ("verdana",21),relief = "groove",border = 0,command = lambda : numPress('0'))
btn0.pack(side = "left",expand = True,fill = "both")

btnDot = tk.Button(frame5,text = ".",font = ("verdana",21),relief = "groove",border = 0,command = dotPress)
btnDot.pack(side = "left",expand = True,fill = "both")

btnResult = tk.Button(frame5,text = "=",font = ("verdana",21),relief = "groove",border = 0,command = result)
btnResult.pack(side = "left",expand = True,fill = "both")

main.mainloop()