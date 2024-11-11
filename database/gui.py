import customtkinter as ctk

# Create the root window
# root = ctk.CTk()

# Create the title of the window
# root.title ("My first GUI")

# Set the size of the window
# root.geometryctk ("320x250")

# def button_click():
#     name = entry.get()
#     label.configure(text=f"Hello, {name}")
#     entry.delete(0, "end")

# create a label widget 
# label = ctk.CTkLabel(root, text="Hello world", font=("Arial",20))
# label.pack(pady=20)
# Create a label widget 
# input_label = ctk.CTkLabel(root, text="Enter your name:", font=("Arial",20))
# input_label.pack()

# Create an entry widget
# entry = ctk.CTkEntry(root, width=200)
# entry.pack(pady=10)

# button = ctk.CTkButton(root, text="Click me", command=button_click)
# button.pack()















    
import customtkinter as ctk



# build a tkinter app that can calculate something

# Set up the main window
root = ctk.CTk()
root.title("simple calculator")

root.geometry("500x500")

# Create labels for the entry fields
label1 = ctk.CTkLabel(root, text="Enter number:")
label1.grid(row=0, column=1)

# Create an entry fields
entry1 = ctk.CTkTextbox(root, width=400)
entry1.grid(row =1, column =1,padx =10, pady =10)


def calculate():
    num1 = entry1.get(1.0, "end")
    result = sum(num1)
    print(num1)
#     print(total)
    return result

calculate()
    
# create buttons for each operation
button_add = ctk.CTkButton(root, text="1", command=lambda: entry1.insert("end", "1"))
button_add.grid(row=4, column=1, padx=5, pady=5)
buton_subtract = ctk.CTkButton(root, text="2", command=lambda: entry1.insert("end", "2"))
buton_subtract.grid(row=4, column=2, padx=5, pady=5)
button_multiply = ctk.CTkButton(root,text="+", command=lambda: entry1.insert("end", "+"))
button_multiply.grid(row=5, column=1, padx=5, pady=5)
button_divide = ctk.CTkButton(root,text="=",command= calculate())
button_divide.grid(row=5,column=2, padx=5, pady = 5)

# create label to display result 
result_label =ctk.CTkLabel(root,text=f"Result: ")
result_label.grid(row=6,column=0, pady=10, columnspan=2)

result_label.configure(text=f"Result:{calculate()}")
# if ValueError:
#         ("Error","Cannot divide by zero")

# run the main loop
root.mainloop()







    







