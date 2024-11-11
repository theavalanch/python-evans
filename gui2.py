from customtkinter import *
import customtkinter

customtkinter.set_appearance_mode("light")

win = CTk()

# Create the title label
win.title("Calculator")

# Set the size of the window
win.geometry("361x315")

# Set the window to be resizable
win.resizable(0, 0)

# Create the entry widget
entry = CTkTextbox(win, width=355, height=50, font=("Arial", 30), fg_color="#bec2c1")
entry.pack()

frame = CTkFrame(win, width=350, fg_color="#25cca2")
frame.pack()

def calculate():
    expression = entry.get(1.0, "end")
    result = eval(expression)
    entry.delete(1.0, "end")
    entry.insert("end", f"={result}")

# First row
btn1 = CTkButton(frame, text="1", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", 1))
btn1.grid(row=1, column=0, padx=5, pady=5)

btn2 = CTkButton(frame, text="2", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", 2))
btn2.grid(row=1, column=1, padx=5, pady=5)

btn3 = CTkButton(frame, text="3", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", 3))
btn3.grid(row=1, column=2, padx=5, pady=5)

plus = CTkButton(frame, text="+", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", "+"))
plus.grid(row=1, column=3, padx=5, pady=5)

# Second row
btn4 = CTkButton(frame, text="4", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", 4))
btn4.grid(row=2, column=0, padx=5, pady=5)

btn5 = CTkButton(frame, text="5", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", 5))
btn5.grid(row=2, column=1, padx=5, pady=5)

btn6 = CTkButton(frame, text="6", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", 6))
btn6.grid(row=2, column=2, padx=5, pady=5)

minus = CTkButton(frame, text="-", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", "+"))
minus.grid(row=2, column=3, padx=5, pady=5)

# Third row
btn7 = CTkButton(frame, text="7", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", 7))
btn7.grid(row=3, column=0, padx=5, pady=5)

btn8 = CTkButton(frame, text="8", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", 8))
btn8.grid(row=3, column=1, padx=5, pady=5)

btn9 = CTkButton(frame, text="9", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", 9))
btn9.grid(row=3, column=2, padx=5, pady=5)

multiply = CTkButton(frame, text="", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", ""))
multiply.grid(row=3, column=3, padx=5, pady=5)

# Fourth row
btn0 = CTkButton(frame, text="0", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", 0))
btn0.grid(row=4, column=0, padx=5, pady=5)

clear = CTkButton(frame, text="⇦", width=80, height=55, font=("Arial", 20) , command=lambda : entry.delete(1.0, "end"))
clear.grid(row=4, column=1, padx=5, pady=5)

equal = CTkButton(frame, text="=", width=80, height=55, font=("Arial", 20), command=calculate)
equal.grid(row=4, column=2, padx=5, pady=5)

divide = CTkButton(frame, text="÷", width=80, height=55, font=("Arial", 20), command=lambda : entry.insert("end", "/"))
divide.grid(row=4, column=3, padx=5, pady=5)






win.mainloop()