import turtle
import random
n = 8
t = []
turtle.delay(0)

for i in range(n):
    nova = turtle.Turtle()
    nova.pu()
    nova.setpos(random.randint(-200, 200), random.randint(-200, 200))
    nova.pencolor(f'#{random.randrange(256**3):06x}')
    nova.pensize(3)
    nova.pd()
    t.append(nova)

while True:
    for i in range(n):
        j = (i+1) % n # index nasledovnej
        uhol = t[i].towards(t[j])
        t[i].seth(uhol)
        vzdialenost = t[i].distance(t[j])
        t[i].fd(vzdialenost / 100)
turtle.done()
