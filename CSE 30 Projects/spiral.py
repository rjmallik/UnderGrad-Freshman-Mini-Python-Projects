import turtle

# draw a spiral
"""
def draw_spiral(t, segments, size, angle):
    t.pendown()
    for i in range(1, segments+1):
        t.fd(size*i)
        t.left(angle)

"""
def draw_spiral(t, segments, size, angle):
    if segments == 0:
        return ""
    draw_spiral(t, segments-1, size, angle)
    t.pendown()
    t.fd(size*segments)
    t.left(angle)

# driver code
if __name__ == '__main__':
    s = turtle.Screen()
    s.setup(400, 400)
    t = turtle.Turtle()
    t.pen(pencolor='dark violet', pensize=2, speed=0)
    t.penup()
    t.home()
    draw_spiral(t, 80, 2, 92)
    input()