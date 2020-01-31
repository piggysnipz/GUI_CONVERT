from tkinter import*

root = Tk()
root.title("SecondsConverter")

units_of_time = ["Minutes","Hours","Days"]
units_of_time_2 = ["Seconds", "Minutes", "Hours"]

var = StringVar(root)
var.set(units_of_time[0])

var_2 = StringVar(root)
var_2.set(units_of_time_2[0])

dropDown = OptionMenu(root,var,*units_of_time)
dropDown.grid(column = 2, row = 2)

dropDown_2 = OptionMenu(root,var_2,*units_of_time_2)
dropDown_2.grid(column=2, row = 1)

label_1 = Label(root,text = "CONVERT ------>")
label_1.grid(column = 1, row = 1)

label_2 = Label(root, text = "TO ------>")
label_2.grid(column =1 , row =2)

entry_1 = Entry(root, width = 35, borderwidth =5)
entry_1.grid(column = 2, row =3)

def calculate(*args):
        num = int(entry_1.get())
        entry_1.delete(0, END)

        if var_2.get() == "Seconds":
            if var.get() == "Minutes":
                entry_1.insert(0,num / 60)
            if var.get() == "Hours":
                entry_1.insert(0,num / 3600)
            if var.get() == "Days":
                entry_1.insert(0,num / 86400)

        if var_2.get() == "Minutes":
            if var.get() == "Minutes":
                entry_1.insert(0,"1")
            if var.get() == "Hours":
                entry_1.insert(0, num / 60)
            if var.get() == "Days":
                entry_1.insert(0,num / 1440)
                

        if var_2.get() == "Hours":
            if var.get() == "Minutes":
                entry_1.insert(0,num * 60)
            if var.get() == "Hours":
                entry_1.insert(0, num * 1)
            if var.get() == "Days":
                entry_1.insert(0,num / 24)

try:
    firstButton = Button(root,text="Calculate",padx=5,pady=5, command = calculate)
    firstButton.grid(column =2, row =4)
        
    root.mainloop()

except: print("An Error has occured")
