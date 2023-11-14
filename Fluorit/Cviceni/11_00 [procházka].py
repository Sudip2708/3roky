import turtle
import random
turtle.delay(0)
t = turtle.Turtle()
for i in range(10000):
    t.seth(random.randint(0, 359))
    t.fd(10)
turtle.done()
