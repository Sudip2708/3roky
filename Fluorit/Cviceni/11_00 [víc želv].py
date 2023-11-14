import turtle
turtle.delay(0)
zoznam = []

for i in range(60):
    t = turtle.Turtle()
    t.pu()
    t.setpos(-300 + 10*i, 0)
    t.pd()
    t.seth(i * 18)
    zoznam.append(t)

##for t in zoznam:
##    for i in range(24):
##        t.fd(20)
##        t.lt(15)

for i in range(24):
    for t in zoznam:
        t.fd(20)
        t.lt(15)
turtle.done()
