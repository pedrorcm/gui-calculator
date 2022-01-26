from tkinter import *
from math import sqrt

def button_click(number):
  current = entrybox.get()
  entrybox.delete(0, END)
  entrybox.insert(0, str(current) + str(number))

def clear_button():
  entrybox.delete(0, END)

def add_button():
  first_number= entrybox.get()
  global f_num
  global operation
  operation = 'addition'
  f_num = round(float(first_number), 5)
  entrybox.delete(0, END)

def sub_button():
  first_number= entrybox.get()
  global f_num
  global operation
  operation = 'subtraction'
  f_num = round(float(first_number), 5)
  entrybox.delete(0, END)

def multiply_button():
  first_number= entrybox.get()
  global f_num
  global operation
  operation = 'multiplication'
  f_num = round(float(first_number), 5)
  entrybox.delete(0, END)

def divide_button():
  first_number= entrybox.get()
  global f_num
  global operation
  operation = 'division'
  f_num = round(float(first_number), 5)
  entrybox.delete(0, END)

def sqrt_button():
  first_number= entrybox.get()
  global f_num
  f_num = round(float(first_number), 5)
  entrybox.insert(0, round(sqrt(f_num), 5))

def onediv_button():
  first_number= entrybox.get()
  global f_num
  f_num = round(float(first_number), 5)
  entrybox.insert(0, 1/f_num)

def squared_button():
  first_number= entrybox.get()
  global f_num
  f_num = float(first_number)
  entrybox.delete(0, END)
  entrybox.insert(0, float(f_num)**2)

def equal_button():
  second_number = int(entrybox.get())
  entrybox.delete(0, END)

  if operation == 'addition':
    entrybox.insert(0, f_num + int(second_number))
  elif operation == 'subtraction':
    entrybox.insert(0, f_num - int(second_number))
  elif operation == 'multiplication':
    entrybox.insert(0, f_num * int(second_number))
  elif operation == 'division':
    entrybox.insert(0, f_num / int(second_number))



root = Tk()
root.title('Calculator')

entrybox = Entry(root, width=55,borderwidth=5)
entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Define buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: add_button())
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: sub_button())
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: multiply_button())
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: divide_button())
button_sqrt = Button(root, text="√", padx=39, pady=20, command=lambda: sqrt_button())
button_onediv = Button(root, text="1/x", padx=34, pady=20, command=lambda: onediv_button())
button_squared = Button(root, text="x²", padx=38, pady=20, command=lambda: squared_button())
button_equal = Button(root, text="=", padx=86, pady=20, command=lambda: equal_button())
button_clear = Button(root, text="Clear", padx=29, pady=20, command=lambda: clear_button())


#Fix buttons on screen

button_1.grid(row=3 , column=0)
button_2.grid(row=3 , column=1)
button_3.grid(row=3 , column=2)
button_multiply.grid(row=3, column=3)


button_4.grid(row=2 , column=0)
button_5.grid(row=2 , column=1)
button_6.grid(row=2 , column=2)
button_subtract.grid(row=2, column=3)


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)


button_0.grid(row=4 , column=0)
button_clear.grid(row=4,column=1)
button_divide.grid(row=4, column=3)
button_squared.grid(row=4, column=2)


button_sqrt.grid(row=5, column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_onediv.grid(row=5, column=3)





root.mainloop()
