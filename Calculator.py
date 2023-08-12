from tkinter import *
from tkinter import ttk
from math import sqrt

root = Tk()
root.title("Calculator")
root.geometry("450x450")

e = Entry(root, width=65)
e.grid(row=0, column=0, columnspan=4, padx=25, pady=15)

ans = 0
dot = False
Math = ""


def Button_click(number):
    curr = e.get()
    e.delete(0, END)
    e.insert(0, str(curr)+str(number))


def Button_clear():
    e.delete(0, END)
    global ans
    global dot
    global Math
    ans = 0
    dot = False
    Math = ""


def Button_dot():
    global dot
    dot = True
    curr = e.get()
    e.delete(0, END)
    e.insert(0, str(curr)+str('.'))


def Button_add():
    first_num = e.get()
    # global f_num
    global Math
    global ans
    global dot
    Math = "addition"

    if (dot):
        f_num = float(first_num)
    else:
        f_num = int(first_num)
    ans = ans+f_num
    e.delete(0, END)


def Button_equal():
    global ans
    global Math
    global dot
    try:
        second_num = e.get()
        # print("second number collected", second_num)
        e.delete(0, END)
        if Math == "addition":
            if(dot):
                e.insert(0, ans + float(second_num))
            else:
                e.insert(0, ans + int(second_num))
        elif Math == "subtraction":
            if(dot):
                e.insert(0, ans - float(second_num))
            else:
                e.insert(0, ans - int(second_num))
        elif Math == "multiply":
            if(dot):
                # print(ans * float(second_num))
                e.insert(0, ans * float(second_num))
            else:
                e.insert(0, ans * int(second_num))
        elif Math == "divide":
            if(dot):
                e.insert(0, ans / float(second_num))
            else:
                e.insert(0, ans / int(second_num))
        elif Math == "logic":
            if(ans < float(second_num)):
                e.insert(0, "TRUE")
            else:
                e.insert(0, "FALSE")
    except:
        e.insert(0, e.get())


def Button_logic():
    val = e.get()
    if val == "":
        e.insert(0, '-')
    else:
        f_num = e.get()
        e.delete(0, END)
        global Math
        global ans
        global dot
        Math = "logic"
        if(dot):
            ans = float(f_num)

        else:
            ans = int(f_num)


def Button_sub():
    first_num = e.get()
    # global f_num
    global Math
    global ans
    global dot
    Math = "subtraction"

    if (dot):
        f_num = float(first_num)
    else:
        f_num = int(first_num)
    ans = f_num
    e.delete(0, END)


def Button_multiply():
    first_num = e.get()
    # global f_num
    global Math
    global ans
    global dot
    Math = "multiply"
    if (dot):
        f_num = float(first_num)
    else:
        f_num = int(first_num)
    ans = f_num
    e.delete(0, END)


def Button_divide():
    first_num = e.get()
    # global f_num
    global Math
    global ans
    global dot
    Math = "divide"
    f_num = float(first_num)
    ans = f_num
    e.delete(0, END)


def Button_sqrt():
    first_num = e.get()
    e.delete(0, END)
    ans = int(first_num)
    e.insert(0, sqrt(ans))


def Button_fact():
    first_num = e.get()
    e.delete(0, END)
    ans = int(first_num)
    if(ans <= 0):
        e.insert(0, '1')
    else:
        val = 1
        for i in range(ans, 1, -1):
            val = val*i
        e.insert(0, val)


my_font = ("Arial", 10, "bold")

# declaring button
button_1 = Button(root, text="1", padx=25, pady=25, font=my_font,
                  command=lambda: Button_click(1))
button_2 = Button(root, text="2", padx=25, pady=25, font=my_font,
                  command=lambda: Button_click(2))
button_3 = Button(root, text="3", padx=25, pady=25, font=my_font,
                  command=lambda: Button_click(3))
button_4 = Button(root, text="4", padx=25, pady=25, font=my_font,
                  command=lambda: Button_click(4))
button_5 = Button(root, text="5", padx=25, pady=25, font=my_font,
                  command=lambda: Button_click(5))
button_6 = Button(root, text="6", padx=25, pady=25, font=my_font,
                  command=lambda: Button_click(6))
button_7 = Button(root, text="7", padx=25, pady=25, font=my_font,
                  command=lambda: Button_click(7))
button_8 = Button(root, text="8", padx=25, pady=25, font=my_font,
                  command=lambda: Button_click(8))
button_9 = Button(root, text="9", padx=25, pady=25, font=my_font,
                  command=lambda: Button_click(9))
button_0 = Button(root, text="0", padx=25, pady=25, font=my_font,
                  command=lambda: Button_click(0))

button_clear = Button(root, text="C", padx=25, pady=25,
                      font=my_font, command=Button_clear)
button_sqrt = Button(root, text="√x", padx=25, pady=25,
                     font=my_font, command=Button_sqrt)
button_divide = Button(root, text="/", padx=25, pady=25,
                       font=my_font, command=Button_divide)

button_multiply = Button(root, text="*", padx=25, font=my_font,
                         pady=25, command=Button_multiply)
button_add = Button(root, text="+", padx=25, pady=25,
                    font=my_font, command=Button_add)
button_sub = Button(root, text="-", padx=25, pady=25,
                    font=my_font, command=Button_sub)

button_logical = Button(root, text="</-", padx=25, font=my_font,
                        pady=25, command=Button_logic)
button_equal = Button(root, text="=", padx=25, pady=25,
                      font=my_font, command=Button_equal)
button_dot = Button(root, text=".", padx=25, pady=25,
                    font=my_font, command=Button_dot)
button_fact = Button(root, text="!", padx=25, pady=25,
                     font=my_font, command=Button_fact)


# inserting button
button_clear.grid(row=1, column=0)
button_sqrt.grid(row=1, column=1)
button_divide.grid(row=1, column=2)
button_logical.grid(row=1, column=3)


button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_fact.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_dot.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

root.mainloop()
