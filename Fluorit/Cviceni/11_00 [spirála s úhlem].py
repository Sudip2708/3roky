import turtle
import random
turtle.delay(0)
t = turtle.Turtle()
while True:
    uhol = random.randint(30, 170)
    print('spirala s uhlom', uhol)
    for i in range(3, 300, 3):
        t.fd(i)
        t.rt(uhol)
    t.reset()
turtle.done()
