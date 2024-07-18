from tkinter import *
from functools import partial

window = Tk()
window.title("Calculator")
window.geometry("400x650+50+50")

value1 = 0
operand = ""
value2 = 0

btnVal = StringVar()
btnVal.set("0")
output = StringVar()
output.set("0")

label1 = Label(window, textvariable=btnVal, bg="#FFFFFF",
               fg="black", font=("Arial", 28, "bold"),
               width=12, height=1)
label1.place(x=50, y=100)

label2 = Label(window, textvariable=output, bg="#FFFFFF",
               fg="black", font=("Arial", 28, "bold"), width=12, height=1)
label2.place(x=50, y=160)

def append_digit(digit):
    global value1, operand, value2

    if operand == "":
        value1 = value1 * 10 + digit
        btnVal.set(value1)
    else:
        value2 = value2 * 10 + digit
        btnVal.set(str(value1) + str(operand) +str(value2))

def setExp(op):
    global value1,operand
    operand = op
    btnVal.set(str(value1)+op)

def calculate():
    global value1, value2, operand

    if operand == "+":
        result = value1 + value2
        output.set(result)
    elif operand == "-":
        result = value1 - value2
        output.set(result)
    elif operand == "*":
        result = value1 * value2
        output.set(result)
    elif operand == "/":
        result = value1 / value2
        output.set(result)
    value1 = 0
    value2 = 0
    operand = ""

def clear():
    global value1, value2, operand
    value1 = 0
    value2 = 0
    operand = ""
    btnVal.set("0")
    output.set("0")

btn1 = Button(window, text="9", bg="black",
              fg="white", font=("Arial", 15, "bold"),
              width=4, height=2, command=lambda: append_digit(9))
btn1.place(x=50, y=250)

btn2 = Button(window, text="8", bg="black",
              fg="white", font=("Arial", 15, "bold"),
              width=4, height=2, command=lambda: append_digit(8))
btn2.place(x=120, y=250)

btn3 = Button(window, text="7", bg="black",
              fg="white", font=("Arial", 15, "bold"),
              width=4, height=2, command=lambda: append_digit(7))
btn3.place(x=190, y=250)

btn4 = Button(window, text="+", bg="blue",
              fg="white", font=("Arial", 15, "bold"),
              width=4, height=2, command=lambda: setExp("+"))
btn4.place(x=260, y=250)

btn5 = Button(window, text="6", bg="black",
              fg="white", font=("Arial", 15, "bold"),
              width=4, height=2, command=lambda: append_digit(6))
btn5.place(x=50, y=330)

btn6 = Button(window, text="5", bg="black",
              fg="white", font=("Arial", 15, "bold"),
              width=4, height=2, command=lambda: append_digit(5))
btn6.place(x=120, y=330)

btn7 = Button(window, text="4", bg="black",
              fg="white", font=("Arial", 15, "bold"),
              width=4, height=2, command=lambda: append_digit(4))
btn7.place(x=190, y=330)

btn8 = Button(window, text="-", bg="#405D72",
              fg="white", font=("Arial", 15, "bold"),
              width=4, height=2, command=lambda: setExp("-"))
btn8.place(x=260, y=330)

btn9 = Button(window, text="3", bg="black",
              fg="white", font=("Arial", 15, "bold"),
              width=4, height=2, command=lambda: append_digit(3))
btn9.place(x=50, y=410)

btn10 = Button(window, text="2", bg="black",
               fg="white", font=("Arial", 15, "bold"),
               width=4, height=2, command=lambda: append_digit(2))
btn10.place(x=120, y=410)

btn11 = Button(window, text="1", bg="black",
               fg="white", font=("Arial", 15, "bold"),
               width=4, height=2, command=lambda: append_digit(1))
btn11.place(x=190, y=410)

btn12 = Button(window, text="*", bg="#478CCF",
               fg="white", font=("Arial", 15, "bold"),
               width=4, height=2, command=lambda: setExp("*"))
btn12.place(x=260, y=410)

btn13 = Button(window, text="0", bg="black",
               fg="white", font=("Arial", 15, "bold"),
               width=4, height=2, command=lambda: append_digit(0))
btn13.place(x=50, y=490)

btn14 = Button(window, text=".", bg="black",
               fg="white", font=("Arial", 15, "bold"),
               width=4, height=2, command=lambda: append_digit("."))
btn14.place(x=120, y=490)

btn15 = Button(window, text="=", bg="#EF5A6F",
               fg="white", font=("Arial", 15, "bold"),
               width=4, height=2, command=calculate)
btn15.place(x=190, y=490)

btn16 = Button(window, text="/", bg="#50B498",
               fg="white", font=("Arial", 15, "bold"),
               width=4, height=2, command=lambda: setExp("/"))
btn16.place(x=260, y=490)

btn_clear = Button(window, text="C", bg="#EB5B00",
                   fg="white", font=("Arial", 15, "bold"),
                   width=4, height=2, command=clear)
btn_clear.place(x=260, y=570)

window.mainloop()
