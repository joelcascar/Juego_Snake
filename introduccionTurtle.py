#from turtle import *

if __name__ == "__main__":
# Dibujo a mano
    """"
    color("yellow")
    width(3)
    forward(100)
    print(pos())
    left(120)
    forward(100)
    print(pos())
    left(120)
    forward(100)
    print(pos())
    left(30)
    forward(150)
    left(90)
    forward(100)
    left(90)
    forward(150)
    color("blue")
    width(3)
    right(90)
    forward(200)
    right(90)
    forward(150)
    right(90)
    forward(200)
    up()
    right(45)
    backward(200)
    down()
    left(45)
    color("green")
    width(6)
    forward(250)
    up()
    home()
    print(pos())
    clearscreen()
    """
# Dibujamos una telaraña de tres colores azul, rojo y verde
    """
    for steps in range(100):
        for c in ('blue', 'red', 'green'):
            color(c)
            forward(steps)
            right(30)
    clearscreen()
    """
# Estrella dibujada en la parte superior con lineas rojas, rellenas con amarillo
    """"
    color("red")
    fillcolor("yellow")
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()
    """

    """"
    from random import random

    for i in range(100):
        steps = int(random() * 100)
        angle = int(random() * 360)
        right(angle)
        fd(steps)
    mainloop()
    """
    """"
    from turtle import Turtle
    from random import random

    t = Turtle()
    t.screen.title("Object-oriented turtle demo")
    t.screen.bgcolor("orange")
    for i in range(100):
        steps = int(random() * 100)
        angle = int(random() * 360)
        t.right(angle)
        t.fd(steps)
    t.screen.mainloop()
    """
    """
    from turtle import *
    t = Turtle()
    t.screen.tracer(n=2, delay=3000)
    dist = 2
    for i in range(200):
        t.fd(dist)
        t.rt(90)
        dist += 2
    t.screen.mainloop()
    """

    """"
    import turtle as t
    a = 20
    t = t.Turtle()
    t.up()
    t.speed(0)
    t.setpos(0,300)
    t.write("Home = {}".format(a), False, align="center", font=("arial", 16, "bold"))
    t.speed(0)
    t.goto(0,0)
    t.speed("slowest")
    t.shape("square")
    t.color("gray")
    t.goto((200,100),None)
    t.goto((-200,100),None)
    t.screen.mainloop()
    """

    import turtle as t
    t = t.Turtle()
    def f():
        t.fd(50)
        t.lt(60)

    t.screen.onkey(f)
    t.screen.listen()
    t.screen.mainloop()