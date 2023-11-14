import turtle


def kriziky4(n, a):
    if n == 0:
        pass
    else:
        
        for i in range(4):
            t.fd(a)
            t.lt(45)
            kriziky4(n-1, a/3)
            t.fd(-a)
            t.lt(45)
        

        
a = 200
n = 5


t = turtle.Turtle()
t.speed(0)
kriziky4(n, a)


turtle.mainloop()
