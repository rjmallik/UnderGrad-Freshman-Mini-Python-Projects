from tkinter import *
import tkinter.font as font
import numpy as np
from fifteen import Fifteen

def clickButton(value):
    for label in labels:
        if value.get() == 'Shuffle':
            tiles.shuffle()
        if label.get() == '  ':
            empty = labels.index(label)
            temp = labels[labels.index(value)]
            labels[empty].set(value.get())
            temp.set('  ')


if __name__ == '__main__':
    tiles = Fifteen()
    empty = np.where(tiles.tiles == 0)[0][0]

    gui = Tk()
    gui.title("Fifteen")

    font = font.Font(family='Helveca', size='25', weight='bold')

    def addButton(gui, value, pos):
        return Button(gui, textvariable=value, name=str(pos),
        bg='white', fg='black', font=font, height=2, width=5,
        command = lambda : clickButton(value))
    
    text1 = StringVar()
    text1.set('1')
    name1 = 1

    text2 = StringVar()
    text2.set('2')
    name2 = 2

    text3 = StringVar()
    text3.set('3')
    name3 = 3

    text4 = StringVar()
    text4.set('4')
    name4 = 4

    text5 = StringVar()
    text5.set('5')
    name5 = 5

    text6 = StringVar()
    text6.set('6')
    name6 = 6

    text7 = StringVar()
    text7.set('7')
    name7 = 7

    text8 = StringVar()
    text8.set('8')
    name8 = 8

    text9 = StringVar()
    text9.set('9')
    name9 = 9

    text10 = StringVar()
    text10.set('10')
    name10 = 10

    text11 = StringVar()
    text11.set('11')
    name11 = 11

    text12 = StringVar()
    text12.set('12')
    name12 = 12

    text13 = StringVar()
    text13.set('13')
    name13 = 13

    text14 = StringVar()
    text14.set('14')
    name14 = 14

    text15 = StringVar()
    text15.set('15')
    name15 = 15

    text16 = StringVar()
    text16.set('  ')
    name16 = 16

    textshuffle = StringVar()
    textshuffle.set('Shuffle')
    name17 = 17

    b1 = addButton(gui, text1, name1)
    b2 = addButton(gui, text2, name2)
    b3 = addButton(gui, text3, name3)
    b4 = addButton(gui, text4, name4)
    b5 = addButton(gui, text5, name5)
    b6 = addButton(gui, text6, name6)
    b7 = addButton(gui, text7, name7)
    b8 = addButton(gui, text8, name8)
    b9 = addButton(gui, text9, name9)
    b10 = addButton(gui, text10, name10)
    b11 = addButton(gui, text11, name11)
    b12 = addButton(gui, text12, name12)
    b13 = addButton(gui, text13, name13)
    b14 = addButton(gui, text14, name14)
    b15 = addButton(gui, text15, name15)
    b16 = addButton(gui, text16, name16)
    b17 = addButton(gui,textshuffle, name17)

    labels = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14, text15, text16, textshuffle]

    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=1, column=2)
    b4.grid(row=1, column=3)

    b5.grid(row=2, column=0)
    b6.grid(row=2, column=1)
    b7.grid(row=2, column=2)
    b8.grid(row=2, column=3)

    b9.grid(row=3, column=0)
    b10.grid(row=3, column=1)
    b11.grid(row=3, column=2)
    b12.grid(row=3, column=3)

    b13.grid(row=4, column=0)
    b14.grid(row=4, column=1)
    b15.grid(row=4, column=2)
    b16.grid(row=4, column=3)

    b17.grid(row=5, columnspan=4)
    
    gui.mainloop()