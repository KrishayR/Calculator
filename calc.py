import tkinter as tk 

root = tk.Tk()
root.title("Calculator")

operator = ""
result = 0

screen_entry = tk.Entry(
                        root,
                        width=40,
                        borderwidth=5
)
screen_entry.grid(row=0,column=0,columnspan=4,padx=20,pady=15)

def numberPressed(number):
  global operator

  if operator == "":
    current = screen_entry.get()
    screen_entry.delete(0,tk.END)
    screen_entry.insert(0,current + str(number))
  else:
    screen_entry.delete(0,tk.END)
    screen_entry.insert(0,str(number))
    operator=""
  return

def performOperation(sign):
  global operator,result
  operator = sign
  current = int(screen_entry.get())
  if sign == "+":
    result += current
    screen_entry.delete(0,tk.END)
    screen_entry.insert(0,str(result))

button_0 = tk.Button(root,text="0",padx=40,pady="20",command=lambda:numberPressed(0))
button_1 = tk.Button(root,text="1",padx=40,pady="20",command=lambda:numberPressed(1))
button_2 = tk.Button(root,text="2",padx=40,pady="20",command=lambda:numberPressed(2))
button_3 = tk.Button(root,text="3",padx=40,pady="20",command=lambda:numberPressed(3))
button_4 = tk.Button(root,text="4",padx=40,pady="20",command=lambda:numberPressed(4))
button_5 = tk.Button(root,text="5",padx=40,pady="20",command=lambda:numberPressed(5))
button_6 = tk.Button(root,text="6",padx=40,pady="20",command=lambda:numberPressed(6))
button_7 = tk.Button(root,text="7",padx=40,pady="20",command=lambda:numberPressed(7))
button_8 = tk.Button(root,text="8",padx=40,pady="20",command=lambda:numberPressed(8))
button_9 = tk.Button(root,text="9",padx=40,pady="20",command=lambda:numberPressed(9))

button_equal = tk.Button(root,text="=",padx=40,pady=20)

def clear_action():
    global result,operator
    screen_entry.delete(0,tk.END)
    result = 0
    screen_entry.insert(0,str(result))
    operator = ""
    

button_plus = tk.Button(root,text="+",padx=40,pady=20,bg="#FAC42F",command=lambda:performOperation("+"))
button_divide = tk.Button(root,text="÷",padx=40,pady=20,bg="#FAC42F",command=lambda:performOperation("÷"))
button_multiply = tk.Button(root,text="x",padx=40,pady=20,bg="#FAC42F",command=lambda:performOperation("x"))
button_subtract = tk.Button(root,text="-",padx=40,pady=20,bg="#FAC42F",command=lambda:performOperation("-"))
button_clear = tk.Button(root,text="C",padx=40,pady=20,bg="#FAC42F", command=clear_action)



button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)

button_equal.grid(row=4,column=1)

button_divide.grid(row=1,column=3)
button_multiply.grid(row=2,column=3)
button_subtract.grid(row=3,column=3)
button_plus.grid(row=4,column=3)

button_clear.grid(row=4,column=2)


root.mainloop()






