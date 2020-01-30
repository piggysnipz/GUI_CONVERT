from tkinter import*

root = Tk()
root.title("SecondsConverter")

units_of_time = ["Minutes","Hours","Days"]

var = StringVar(root)
var.set(units_of_time[0])

dropDown = OptionMenu(root,var,*units_of_time)
dropDown.pack()

label_1 = Label(root,text="Seconds")
label_1.pack()

entry_1 = Entry(root, width = 35)
entry_1.pack()


global mode

def add_min(sec):
    seconds = entry_1.get()
    minutes = int(seconds) / 60
    adding = Label(root,text="Minutes:" + str(minutes))
    adding.pack()

def add_hour(sec):
    seconds = entry_1.get()
    hours = int(seconds) / 3600
    adding = Label(root,text="Hours:" + str(hours))
    adding.pack()


def add_day(sec):
    seconds = entry_1.get()
    days = int(seconds) / 86400
    adding = Label(root,text="Days:" +str(days))
    adding.pack()

def get_dropdown(*args):
    if(len(entry_1.get()) > 0):
        try:
            #int(5)
            #int(a) WOULD NOT WORK
            placeholder_int = int(entry_1.get())
            if var.get() == "Minutes":
                return add_min(entry_1.get())
            if var.get() == "Hours":
                return add_hour(entry_1.get())
            if var.get() == "Days":
                return add_day(entry_1.get())
        except:
            print("An error has occured. The input field is not an int.")
            adding = Label(root,text="Value not integer")
            adding.pack()

    print (var.get())

var.trace("w", get_dropdown)


try:
    firstButton = Button(root,text="Calculate", command = get_dropdown)
    firstButton.pack()



    root.mainloop()

except: print("An Error has occured")
