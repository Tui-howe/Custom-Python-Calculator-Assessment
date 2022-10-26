# T M Howe
# 22/09/2022

# ***************************************************
# Custom Python Calculator with GUI (Graphic User Interface)
# ***************************************************

from tkinter import * # import the tkinter library

def button_press(num):   # defining each button press
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():   #this block checks for the button_press(equals)
    global equation_text

    try: #try is used in try

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError: # chech for syntax error

        equation_text.set("syntax error")

        equation_text = ""

    except ZeroDivisionError: # check for division by zero

        equation_label.set("Arithmetic error")

        equation_text = ""

def clear(): # Clears the equation_label
    global equation_text

    equation_label.set("")
    equation_text = ""




# Designing the user interface
window = Tk()
window.title("Calculator")
window.geometry("500x500")
window.configure(bg="#ff0000")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('console', 20), bg="#03EC06", width=24, height=1)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, bg = "#F8FF00", text=1, height=4, width=9, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, bg = "#F8FF00", text=2, height=4, width=9, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, bg = "#F8FF00", text=3, height=4, width=9, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, bg = "#F8FF00", text=4, height=4, width=9, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, bg = "#F8FF00", text=5, height=4, width=9, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, bg = "#F8FF00", text=6, height=4, width=9, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, bg = "#F8FF00", text=7, height=4, width=9, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, bg = "#F8FF00", text=8, height=4, width=9, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, bg = "#F8FF00", text=9, height=4, width=9, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, bg = "#F8FF00", text=0, height=4, width=9, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)


# Create operation buttons

plus = Button(frame, bg = "#03EC06", text='+', height=4, width=9, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, bg = "#03EC06", text='-', height=4, width=9, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, bg = "#03EC06", text='x', height=4, width=9, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, bg = "#03EC06", text='÷', height=4, width=9, font=35, command=lambda: button_press('/'))
divide.grid(row=3, column=3)

# Create equals button

equal = Button(frame, bg = "#03EC06", text='=', height=4, width=9, font=35, command=equals)
equal.grid(row=3, column=2)

# Create the decimal button
decimal = Button(frame, bg = "#03EC06", text='.', height=4, width=9, font=35, command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

# Create the clear button

clear = Button(window, bg = "#03EC06", text='Reset', height=4, width=9, font=35, command=clear)
clear.pack()

window.mainloop()
