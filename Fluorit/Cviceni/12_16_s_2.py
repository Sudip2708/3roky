import turtle
t = turtle.Turtle()
t.lt(90)
t.pu()
t.fd(100)
t.rt(30)
t.pd()
def krok():
    t.fd(30)
    t.rt(120)
for i in range(4):
    t.fd(50)
    t.lt(10+20)
    for i in range(3):
        krok()
    t.lt(60)
t.rt(30)
t.fd(70)
for i in range(10):
    pass
turtle.done()