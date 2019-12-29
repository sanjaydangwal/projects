import tkinter as tk
from tkinter import ttk
main_win = tk.Tk()
main_win.title("Quizze")


Container = ttk.LabelFrame(main_win,text = "Select")


# ----------------classes----------------
class Admin():
    def __init__(self):
        self.userName = None
        self.password = None

    def logIn(self,Container):
        for widgit in Container.winfo_children():
            widgit.destroy()
    def Admin_panel(self,Container):
        for widgit in Container.winfo_children():
            widgit.destroy()
        Container['text'] = "LOG IN/SIGN UP"
        self.userName = tk.StringVar()
        self.password = tk.StringVar()
        ttk.Button(Container,text = "LOG IN",command =lambda : adm.logIn(Container)).grid(row = 0,column = 0,sticky =tk.W)
        ttk.Button(Container,text = "SIGN UP").grid(row = 1,column = 0,sticky =tk.W)



#----------main panel-----------------




    




       


        
    






adm = Admin()

ttk.Button(Container,text = "Admin",command = lambda: adm.Admin_panel(Container)).grid(row = 0,column = 0)
print(adm.userName)
# for widget in main_win.winfo_children():
#     widget.destroy()

Container.grid(row = 0,column = 0,padx = 10,pady = 10)

main_win.geometry("500x300")

main_win.mainloop()