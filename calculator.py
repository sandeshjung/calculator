from tkinter import *

root =Tk()
root.title("Simple Calculator")

e = Entry(root,width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def _button(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0,END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = float(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    e.delete(0,END)

def button_division():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,f_num + float(second_number))
    if math == "subtraction":
        e.insert(0,f_num - float(second_number))
    if math == "multiply":
        e.insert(0,f_num * float(second_number))
    if math == "division":
        e.insert(0,f_num / float(second_number))

def button_clear():
    e.delete(0,END)

button_1 = Button (root, text="1", padx=40, pady=20, command=lambda : _button(1))
button_2 = Button (root, text="2", padx=40, pady=20, command=lambda : _button(2))
button_3 = Button (root, text="3", padx=40, pady=20, command=lambda : _button(3))
button_4 = Button (root, text="4", padx=40, pady=20, command=lambda : _button(4))
button_5 = Button (root, text="5", padx=40, pady=20, command=lambda : _button(5))
button_6 = Button (root, text="6", padx=40, pady=20, command=lambda : _button(6))
button_7 = Button (root, text="7", padx=40, pady=20, command=lambda : _button(7))
button_8 = Button (root, text="8", padx=40, pady=20, command=lambda : _button(8))
button_9 = Button (root, text="9", padx=40, pady=20, command=lambda : _button(9))
button_0 = Button (root, text="0", padx=40, pady=20, command=lambda : _button(0))
button_dot= Button (root, text=".", padx=41, pady=20, command=lambda : _button())
button_add = Button (root, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button (root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button (root, text="*", padx=40, pady=20, command=button_multiply)
button_division = Button (root, text="/", padx=40, pady=20, command=button_division)
button_equal=Button (root, text="=", padx=39, pady=20, command=button_equal)
button_clear = Button(root, text="C", padx=30, pady=15, command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_dot.grid(row=4, column=0)
button_add.grid(row=4, column=2)

button_clear.grid(row=0, column=4)
button_equal.grid(row=4, column=4)

button_multiply.grid(row=1, column=4)
button_subtract.grid(row=2, column=4)
button_division.grid(row=3, column=4)

root.mainloop()
