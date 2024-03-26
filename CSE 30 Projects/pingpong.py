from tkinter import *

def move_left(*args):
    canvas.move(racket_id, -50, 0)
    
def move_right(*args):
    canvas.move(racket_id, 50, 0)
    
def animation():
    global dx
    global dy
    global playerScore
    global aiScore
    a1, b1, a2, b2 = canvas.coords(ball)

    if a2 > width or a1 < 0:
        dx = - dx
    if b2 > height:
        dy = - dy
        playerScore += 1
    if  b1 < 0:
        dy = - dy
        aiScore += 1
    
    px1, py1, px2, py2 = canvas.coords(racket_id)

    if (a2 < px2 and a1 > px1) and (b1 < 20 ):
        dy = - dy

    px1, py1, px2, py2 = canvas.coords(racket_AI)
    
    if (a2 < px2 and a1 > px1) and (b2 > 580):
        dy = - dy

    canvas.move(ball,dx,dy)
    canvas.itemconfig(text_id, text='Score' + ' ' + str(playerScore) + ':' + str(aiScore))
    canvas.after(10, animation)

def moveAI():
    a1, b1, a2, b2 = canvas.coords(ball)
    xa1, xb1, xa2, xb2 = canvas.coords(racket_AI)

    if a1 < xa1:
        canvas.move(racket_AI, -25, 0)
    if a2 > xa2:
        canvas.move(racket_AI, 25, 0)
    canvas.after(10, moveAI)

#main program
gui = Tk()
canvas = Canvas(gui, bd='3', width='600', height='600')

playerScore = 0
aiScore = 0

ball = canvas.create_oval(100,100,125,125, fill = 'red')
racket_id = canvas.create_rectangle(250, 10, 350, 20, fill='black')
canvas.bind_all('<KeyPress-Left>', move_left)
canvas.bind_all('<KeyPress-Right>', move_right)

racket_AI = canvas.create_rectangle(250, 580, 350, 590, fill='blue')

text_id = canvas.create_text(100, 100, text='Score' + str(playerScore) + ':' + str(aiScore), font=('Times', 20))

canvas.pack()
width = int(canvas.cget('width'))
height = int(canvas.cget('height'))
dx,dy = 1, 1
animation()
moveAI()
mainloop()