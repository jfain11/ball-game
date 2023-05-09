import turtle
from random import randint

wn = turtle.Screen()
wn.bgcolor("white")
wn.tracer(0)
wn.setup(width=1000, height=800)
wn.bgcolor("light sky blue")

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 340)

t1 = turtle.Turtle()
t1.shape('circle')
t1.penup()
t1.setposition(randint(-490, 490), randint(-390, 390))

# Player

player = turtle.Turtle()
player.speed(0)
player.shape("circle")
player.color("red")
player.shapesize(1.5, 1.5, 1.5)
player.penup()
player.goto(0, 0)


def go_up():
    y = player.ycor()
    y += 1
    player.sety(y)


def go_down():
    y = player.ycor()
    y -= 1
    player.sety(y)


def go_left():
    x = player.xcor()
    x -= 1
    player.setx(x)


def go_right():
    x = player.xcor()
    x += 1
    player.setx(x)


score = 0
pen.write(score, align="center", font=("Courier", 30, "bold"))

while True:
    wn.update()

    if player.ycor() == t1.ycor() and player.xcor() >= t1.xcor():
        go_left()
    if player.ycor() == t1.ycor() and player.xcor() <= t1.xcor():
        go_right()
    if player.ycor() <= t1.ycor() and player.xcor() == t1.xcor():
        go_up()
    if player.ycor() >= t1.ycor() and player.xcor() >= t1.xcor():
        go_down()
    elif player.ycor() <= t1.ycor():
        y = player.ycor()
        y += 1
        player.sety(y)
    elif player.ycor() >= t1.ycor():
        y = player.ycor()
        y -= 1
        player.sety(y)

    if player.distance(t1) < 20:
        t1.goto(randint(-480, 480), randint(-380, 380))
        t1.color("black")
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.ycor() > 390:
        wn.clearscreen()

    if player.ycor() < -390:
        wn.clearscreen()

    if player.xcor() > 490:
        wn.clearscreen()

    if player.xcor() < -490:
        wn.clearscreen()

turtle.mainloop()
