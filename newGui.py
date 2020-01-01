import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
# import os
# from csv import DictWriter
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "dangwal680",
    database = "db1"
)

win = tk.Tk()
win.title("Submission form")
# win.config(background = "Blue")
filds = ('Full Name  :  ','Email Address  :  ','Age  :  ','Mobile Number  :  ','Gender  :  ')
cantainer = ttk.Labelframe(win,text = "User Details")
# cantainer.configure(background = "SystemWindow")
cantainer.grid(row = 0,column = 0,padx= 5,pady = 5)

for i in range(len(filds)):
    label = ttk.Label(cantainer,text = filds[i])
    label.grid(row = i , column = 0,sticky = tk.W, pady = 3,padx = 3) 
fieldValues = {
    'Full Name':tk.StringVar(),
    'Email Address':tk.StringVar(),
    'Age':tk.StringVar(),
    'Mobile Number':tk.StringVar(),
    'Gender':tk.StringVar(),
    'Type': tk.StringVar(),
    'Subscribe': tk.IntVar()
}
count = 0
boxs = []
for i in fieldValues:
    if i == 'Gender':
        comboBox = ttk.Combobox(cantainer,values = ['Male','Female','Other'],state = "readonly",textvariable = fieldValues[i],width = 14)
        comboBox.current(0)
        comboBox.grid(row = count , column = 1)
    elif i == 'Type':
        radiobtn1 = ttk.Radiobutton(cantainer,value = "Student",text = "Student",variable = fieldValues[i])
        radiobtn1.grid(row = count,column = 0)
        radiobtn1 = ttk.Radiobutton(cantainer,value = "Teacher",text = "Teacher",variable = fieldValues[i])
        radiobtn1.grid(row = count,column = 1)
    elif i == 'Subscribe':
        userSubscribe = ttk.Checkbutton(cantainer,text = "Subscribe",variable = fieldValues[i])
        userSubscribe.grid(row = count , columnspan = 2)
    else:
        box = ttk.Entry(cantainer,width = 15,textvariable = fieldValues[i],show = "")
        box.grid(row = count,column = 1,padx = 10,pady = 3)
        boxs.append(box)
        if i=='Full Name':
            box.focus()
    count +=1
'''
def action():
    with open("data.csv","a",newline="") as wf:
        csv_writer = DictWriter(wf,fieldnames = fieldValues)
        if os.stat('data.csv').st_size == 0:
            csv_writer.writeheader()
        if fieldValues.get("Subscribe").get == 0:
            Subscribe = 'No'
        else:
            Subscribe = 'Yes'
        csv_writer.writerow(
             {
                 'Full Name':fieldValues.get("Full Name").get(),
                 'Email Address':fieldValues.get("Email Address").get(),
                 'Age':fieldValues.get("Age").get(),
                 'Mobile Number':fieldValues.get("Mobile Number").get(),
                 'Gender':fieldValues.get("Gender").get(),
                 'Type': fieldValues.get("Type").get(),
                 'Subscribe': Subscribe
            }
        )
        for box in boxs:
            box.delete(0,tk.END)
'''
def action2():
    curr = mydb.cursor()
    # print(fieldValues.get('Full Name').get())
    user_name = fieldValues.get('Full Name').get()
    user_email = fieldValues.get('Email Address').get()
    user_age = fieldValues.get('Age').get()
    user_mobile = fieldValues.get('Mobile Number').get()
    user_gender = fieldValues.get('Gender').get()
    user_type = fieldValues.get('Type').get()
    user_subscribe = ""
    if fieldValues.get('Subscribe').get == 0:
        user_subscribe = 'no'
    else:
        user_subscribe = 'yes'
    try:
        curr.execute("INSERT INTO DATA2(full_name,email_address,age,mobile_number,gender,type,subscribe) VALUES(%s,%s,%s,%s,%s,%s,%s)",(user_name,user_email,user_age,user_mobile,user_gender,user_type,user_subscribe))
        mydb.commit()
        for box in boxs:
            box.delete(0,tk.END)
    except mysql.connector.ProgrammingError:
        m_box.showerror("ERROR","DATABASE CONNECTIVITY FAILED")
    except mysql.connector.errors.IntegrityError:
        m_box.showwarning('warning','user already exist')

submitButton = ttk.Button(win,text = "Submit",command = action2)
submitButton.grid(row = 1,column = 0,pady = 3)
win.mainloop()
