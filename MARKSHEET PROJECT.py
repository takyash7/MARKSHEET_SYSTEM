import tkinter as tk
from tkinter import messagebox
from tkinter import *

master = tk.Tk()

master.title('''MARKSHEET OF STUFENT 
                POORNINMA INSTITUTE OF ENGINEERING AND TECNNOLOGY''')

master.geometry("1500x1200")

e1 = tk.Entry(master,font=1,justify="center")
e2 = tk.Entry(master,font=1,justify="center")
e3 = tk.Entry(master,font=1,justify="center")
e4 = tk.Entry(master,font=1,justify="center")
e5 = tk.Entry(master,font=1,justify="center")
e6 = tk.Entry(master,font=1,justify="center")
e7 = tk.Entry(master,font=1,justify="center")
e8 = tk.Entry(master,font=1,justify="center")
e10 = tk.Entry(master,font=1,justify="center")
e11 = tk.Entry(master,font=1,justify="center")
e12 = tk.Entry(master,font=1,justify="center")
e13 = tk.Entry(master,font=1,justify="center")


def display():
    
    entries = [e1, e2, e3, e4, e5, e6, e7, e8, e9,e10,e11,e12,e13]

    for entry in entries:
        if entry.get() == "":
            messagebox.showerror("Error", "All fields are mandatory")
            return
    
    tot = 0
    
    mark_e4 = int(e4.get())
    mark_e5 = int(e5.get())
    mark_e6 = int(e6.get())
    mark_e7 = int(e7.get())
    mark_e8 = int(e8.get())
   
    if mark_e4 > 80 and mark_e4 <= 100:
        tk.Label(master, fg="green",text=5,font=10).grid(row=4, column=5)
        tot += 5
    if mark_e4 > 60 and mark_e4 <=80:
        tk.Label(master, fg="green",text=4,font=10).grid(row=4, column=5)
        tot += 4
    if mark_e4 >40 and mark_e4 <= 60:
        tk.Label(master, fg="green",text=3,font=10).grid(row=4, column=5)
        tot += 3
    if mark_e4 > 20 and mark_e4 <= 40:
        tk.Label(master, fg="red",text=2,font=10).grid(row=4, column=5)
        tot += 2
    if mark_e4 >=1 and mark_e4 <= 20:
        tk.Label(master, fg="red",text=1,font=10).grid(row=4, column=5)
        tot += 1
    if mark_e4 == 0 :
        tk.Label(master, fg="red",text=0,font=10).grid(row=4, column=5)
        tot += 0  
    
    if mark_e5 > 80 and mark_e5 <= 100:
        tk.Label(master, fg="green",text=5,font=10).grid(row=5, column=5)
        tot += 5
    if mark_e5> 60 and mark_e5 <=80:
        tk.Label(master, fg="green",text=4,font=10).grid(row=5, column=5)
        tot += 4
    if mark_e5 >40 and mark_e5 <= 60:
        tk.Label(master, fg="green",text=3,font=10).grid(row=5, column=5)
        tot += 3
    if mark_e5 > 20 and mark_e5 <= 40:
        tk.Label(master, fg="red",text=2,font=10).grid(row=5, column=5)
        tot += 2
    if mark_e5 >=1 and mark_e5 <= 20:
        tk.Label(master, fg="red",text=1,font=10).grid(row=5, column=5)
        tot += 1
    if mark_e5 == 0 :
        tk.Label(master, fg="red",text=0,font=10).grid(row=5, column=5)
        tot += 0

    if mark_e6 > 80 and mark_e6 <= 100:
        tk.Label(master, fg="green",text=5,font=10).grid(row=6, column=5)
        tot += 5
    if mark_e6 > 60 and mark_e6 <=80:
        tk.Label(master, fg="green",text=4,font=10).grid(row=6, column=5)
        tot += 4
    if mark_e6 >40 and mark_e6 <= 60:
        tk.Label(master, fg="green",text=3,font=10).grid(row=6, column=5)
        tot += 3
    if mark_e6 > 20 and mark_e6 <= 40:
        tk.Label(master, fg="red",text=2,font=10).grid(row=6, column=5)
        tot += 2
    if mark_e6 >=1 and mark_e6 <= 20:
        tk.Label(master, fg="red",text=1,font=10).grid(row=6, column=5)
        tot += 1
    if mark_e6 == 0 :
        tk.Label(master, fg="red",text=0,font=10).grid(row=6, column=5)
        tot += 0

    if mark_e7 > 80 and mark_e7 <= 100:
        tk.Label(master, fg="green",text=5,font=10).grid(row=7, column=5)
        tot += 5
    if mark_e7 > 60 and mark_e7 <=80:
        tk.Label(master, fg="green",text=4,font=10).grid(row=7, column=5)
        tot += 4
    if mark_e7 >40 and mark_e7 <= 60:
        tk.Label(master, fg="green",text=3,font=10).grid(row=7, column=5)
        tot += 3
    if mark_e7 > 20 and mark_e7 <= 40:
        tk.Label(master, fg="red",text=2,font=10).grid(row=7, column=5)
        tot += 2
    if mark_e7 >=1 and mark_e7 <= 20:
        tk.Label(master, fg="red",text=1,font=10).grid(row=7, column=5)
        tot += 1
    if mark_e7 == 0 :
        tk.Label(master, fg="red",text=0,font=10).grid(row=7, column=5)
        tot += 0 
        
    if mark_e8 > 80 and mark_e8 <= 100:
        tk.Label(master, fg="green",text=5,font=10).grid(row=8, column=5)
        tot += 5
    if mark_e8 > 60 and mark_e8 <=80:
        tk.Label(master, fg="green",text=4,font=10).grid(row=8, column=5)
        tot += 7
    if mark_e8 >40 and mark_e8 <= 60:
        tk.Label(master, fg="green",text=3,font=10).grid(row=8, column=5)
        tot += 3
    if mark_e8 > 20 and mark_e8 <= 40:
        tk.Label(master, fg="red",text=2,font=10).grid(row=8, column=5)
        tot += 2
    if mark_e8 >=1 and mark_e8 <= 20:
        tk.Label(master, fg="red",text=1,font=10).grid(row=8, column=5)
        tot += 1
    if mark_e8 == 0 :
        tk.Label(master, fg="red",text=0,font=10).grid(row=8, column=5)
        tot += 0 
        
    tk.Label(master, text=str(tot),font=30).grid(row=12, column=5)
    tk.Label(master, text=str((tot/25)*10),font=30).grid(row=13, column=5)
    
    if mark_e4 <= 40:
        tk.Label(master, text="Back",font=20,fg="red").grid(row=17, column=3)
    else:
        tk.Label(master, text="None",font=20,fg="green").grid(row=17, column=3)
    if mark_e5 <= 40:
        tk.Label(master, text="Back",font=20,fg="red").grid(row=18, column=3)
    else:
        tk.Label(master, text="None",font=20,fg="green").grid(row=18, column=3)     
    if mark_e6 <= 40:
        tk.Label(master, text="Back",font=20,fg="red").grid(row=19, column=3)
    else:
        tk.Label(master, text="None",font=20,fg="green").grid(row=19, column=3)
    if mark_e7 <= 40:
        tk.Label(master, text="Back",font=20,fg="red").grid(row=20, column=3)
    else:
        tk.Label(master, text="None",font=20,fg="green").grid(row=20, column=3)
    if mark_e8 <= 40:
        tk.Label(master, text="Back",font=20,fg="red").grid(row=21, column=3)
    else:
        tk.Label(master, text="None",font=20,fg="green").grid(row=21, column=3)
    
tk.Label(master, fg="blue",text="Name",font=20).grid(row=0, column=1)
tk.Label(master, fg="blue",text="Semester",font=20).grid(row=0, column=4)
tk.Label(master, fg="blue",text="Roll.No",font=20).grid(row=1, column=1)
tk.Label(master, fg="blue",text="Section",font=20).grid(row=1, column=4)

tk.Label(master, fg="blue",text="Srl.No",font=20).grid(row=3, column=1)
tk.Label(master, text="1",font=20).grid(row=4, column=1)
tk.Label(master, text="2",font=20).grid(row=5, column=1)
tk.Label(master, text="3",font=20).grid(row=6, column=1)
tk.Label(master, text="4",font=20).grid(row=7, column=1)
tk.Label(master, text="5",font=20).grid(row=8, column=1)

tk.Label(master,fg="blue", text="Subjects",font=20).grid(row=3, column=2)
tk.Label(master, text=" Math  201",font=2).grid(row=4, column=2)
tk.Label(master, text="Physics   202",font=2).grid(row=5, column=2)
tk.Label(master, text="BME  204",font=2).grid(row=6, column=2)
tk.Label(master, text="BCE  208",font=2).grid(row=7, column=2)
tk.Label(master, text="Comm.Skils  206",font=2).grid(row=8, column=2)

tk.Label(master,fg="blue", text="Marks",font=20).grid(row=3, column=3)
e4.grid(row=4, column=3)
e5.grid(row=5, column=3)
e6.grid(row=6, column=3)
e7.grid(row=7, column=3)
e8.grid(row=8, column=3)

tk.Label(master,fg="blue", text="Sub Credit",font=20).grid(row=3, column=4)
tk.Label(master, text="5",font=10).grid(row=4, column=4)
tk.Label(master, text="5",font=10).grid(row=5, column=4)
tk.Label(master, text="5",font=10).grid(row=6, column=4)
tk.Label(master, text="5",font=10).grid(row=7, column=4)
tk.Label(master, text="5",font=10).grid(row=8, column=4)

tk.Label(master,fg="blue",text="Credit Obtained",font=20).grid(row=3, column=5)

e1 = tk.Entry(master,font=1,justify="center")
e1.focus_set()
e2 = tk.Entry(master,font=1,justify="center")
e3 = tk.Entry(master,font=1,justify="center")
e9 = tk.Entry(master,font=1,justify="center")

e1.grid(row=0, column=2)
e2.grid(row=0, column=5)
e3.grid(row=1, column=2)
e9.grid(row=1, column=5)

e10.grid(row=18, column=5)
e11.grid(row=19, column=5)
e12.grid(row=20, column=5)
e13.grid(row=21, column=5)

button1 = tk.Button(master, text="SUBMIT",font=20, bg="white",fg="red", command=display)
#button1.grid(row=5, column=5)
button1.place(x=710,y=560)

tk.Label(master,fg="blue", text="Total Credit",font=20).grid(row=12, column=4)
tk.Label(master,fg="blue", text="CGPA",font=20).grid(row=13, column=4)

tk.Label(master,fg="blue", text="BACK",font=15).grid(row=16, column=2)
tk.Label(master,fg="blue", text="(If Any)",font=15).grid(row=16, column=3)
tk.Label(master, text="Math  201",font=5).grid(row=17, column=2)
tk.Label(master, text="Physics  202",font=5).grid(row=18, column=2)
tk.Label(master, text="BME  204",font=5).grid(row=19, column=2)
tk.Label(master, text="BCE  208",font=5).grid(row=20, column=2)
tk.Label(master, text="Comm.Skills  206",font=5).grid(row=21, column=2)

tk.Label(master,fg="blue", text="DECA",font=15).grid(row=17, column=4)
tk.Label(master,fg="blue", text="Grade",font=15).grid(row=17, column=5)
tk.Label(master, text="Attendance",font=15).grid(row=18, column=4)
tk.Label(master, text="Assigment",font=15).grid(row=19, column=4)
tk.Label(master,text="Project",font=15).grid(row=20, column=4)
tk.Label(master, text="Activity",font=15).grid(row=21, column=4)

tk.Label(master,text="                                                                                                               ").grid(row=11, column=0)
tk.Label(master).grid(row=2, column=0)

master.mainloop()


