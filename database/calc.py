import customtkinter as ctk

# Initialize custom tkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Initialize the main window
app = ctk.CTk()
app.geometry("400x500")
app.title("Continuous Calculator")

# Define entry widget to display the input and results
display = ctk.CTkEntry(app, width=350, height=50, font=("Arial", 24), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Variables
current_input = ""

# Function to update input in the entry widget
def update_display(value):
    global current_input
    if current_input and current_input[-1] in "+-/" and value in "+-/":
        # Avoid adding multiple consecutive operators
        current_input = current_input[:-1] + value
    else:
        current_input += str(value)
    display.delete(0, ctk.END)
    display.insert(ctk.END, current_input)

# Function to clear the display
def clear_display():
    global current_input
    current_input = ""
    display.delete(0, ctk.END)

# Function to evaluate and display continuous result
def calculate():
    global current_input
    try:
        result = eval(current_input)  # Evaluate the input expression
        display.delete(0, ctk.END)
        display.insert(ctk.END, result)
        current_input = str(result)  # Update current input with the result
    except Exception:
        display.delete(0, ctk.END)
        display.insert(ctk.END, "Error")
        current_input = ""

# Define button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        button = ctk.CTkButton(app, text=text, width=80, height=60, font=("Arial", 20), command=calculate)
    elif text == "C":
        button = ctk.CTkButton(app, text=text, width=80, height=60, font=("Arial", 20), command=clear_display)
    else:
        button = ctk.CTkButton(app, text=text, width=80, height=60, font=("Arial", 20), command=lambda x=text: update_display(x))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the main loop
app.mainloop()













































