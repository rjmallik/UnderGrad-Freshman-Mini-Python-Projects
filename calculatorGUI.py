from tkinter import *
from calculator import *

current = ''

def calculator(gui):   
    gui.title("Calculator")
    entrybox = Entry(gui, width=36, borderwidth=5, textvariable =solve)
    entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    
    b0 = addButton(gui,entrybox,'0')
    b1 = addButton(gui,entrybox,'1')
    b2 = addButton(gui,entrybox,'2')
    b3 = addButton(gui,entrybox,'3')
    b4 = addButton(gui,entrybox,'4')
    b5 = addButton(gui,entrybox,'5')
    b6 = addButton(gui,entrybox,'6')
    b7 = addButton(gui,entrybox,'7')
    b8 = addButton(gui,entrybox,'8')
    b9 = addButton(gui,entrybox,'9')
    b_add = addButton(gui,entrybox,'+')
    b_sub = addButton(gui,entrybox,'-')
    b_mult = addButton(gui,entrybox,'*')
    b_div = addButton(gui,entrybox,'/')
    b_clr = addButton(gui,entrybox,'c')
    b_eq = addButton(gui,entrybox,'=')

    buttons =[ b7,    b8, b9,    b_clr, 
               b4,    b5, b6,    b_sub, 
               b1,    b2, b3,    b_add, 
               b_mult,b0, b_div, b_eq ]
    holder = 4           
    for i in range(holder):
        for j in range(holder):
            buttons[i*holder+j].grid(row=i+1, column=j, columnspan=1)

def addButton(gui, entrybox, value):
    return Button(gui, text=value, height=4, width=9, command = lambda: clickButton(entrybox, value))

current = ''
def clickButton(entrybox, value):
    if value == '=':
        answer = calculate(current)
        solve.set(answer)
        current = ''
    elif value == 'c':
        current = ''
        solve.set('')
    else:
        current += value
        solve.set(current)
    
gui = Tk()
solve = StringVar()
calculator(gui)
gui.mainloop()