# MAZE GAME
# Get from one start to finish.
# If player hits the wall of the maze they lose and restart.
# If they finish they win
# player should be constantly moving at a determined speed
import turtle
from random import randint

wn = turtle.Screen()
wn.bgcolor("white")
wn.tracer(0)
wn.setup(width=1000, height=800)
wn.bgcolor("light sky blue")


score = 0

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

t2 = turtle.Turtle()
t2.shape('circle')
t2.penup()
t2.goto(randint(-490, 490), randint(-390, 390))

t3 = turtle.Turtle()
t3.shape('circle')
t3.penup()
t3.goto(randint(-490, 490), randint(-390, 390))

t4 = turtle.Turtle()
t4.shape('circle')
t4.penup()
t4.goto(randint(-490, 490), randint(-390, 390))

t5 = turtle.Turtle()
t5.shape('circle')
t5.penup()
t5.goto(randint(-490, 490), randint(-390, 390))

t6 = turtle.Turtle()
t6.shape('circle')
t6.penup()
t6.goto(randint(-490, 490), randint(-390, 390))

t7 = turtle.Turtle()
t7.shape('circle')
t7.penup()
t7.goto(randint(-490, 490), randint(-390, 390))

t8 = turtle.Turtle()
t8.shape('circle')
t8.penup()
t8.setposition(randint(-490, 490), randint(-390, 390))

t9 = turtle.Turtle()
t9.shape('circle')
t9.penup()
t9.goto(randint(-490, 490), randint(-390, 390))

t10 = turtle.Turtle()
t10.shape('circle')
t10.penup()
t10.goto(randint(-490, 490), randint(-390, 390))

t11 = turtle.Turtle()
t11.shape('circle')
t11.penup()
t11.goto(randint(-490, 490), randint(-390, 390))

t12 = turtle.Turtle()
t12.shape('circle')
t12.penup()
t12.goto(randint(-490, 490), randint(-390, 390))

t13 = turtle.Turtle()
t13.shape('circle')
t13.penup()
t13.goto(randint(-490, 490), randint(-390, 390))

t14 = turtle.Turtle()
t14.shape('circle')
t14.penup()
t14.goto(randint(-490, 490), randint(-390, 390))

t15 = turtle.Turtle()
t15.shape('circle')
t15.penup()
t15.goto(randint(-490, 490), randint(-390, 390))

t16 = turtle.Turtle()
t16.shape('circle')
t16.penup()
t16.goto(randint(-490, 490), randint(-390, 390))

t17 = turtle.Turtle()
t17.shape('circle')
t17.penup()
t17.goto(randint(-490, 490), randint(-390, 390))

t18 = turtle.Turtle()
t18.shape('circle')
t18.penup()
t18.goto(randint(-490, 490), randint(-390, 390))

t19 = turtle.Turtle()
t19.shape('circle')
t19.penup()
t19.goto(randint(-490, 490), randint(-390, 390))

t20 = turtle.Turtle()
t20.shape('circle')
t20.penup()
t20.goto(randint(-490, 490), randint(-390, 390))

# Player

player = turtle.Turtle()
player.speed(0)
player.shape("circle")
player.color("red")
player.shapesize(1.5, 1.5, 1.5)
player.penup()
player.goto(0, 0)

# CONSTANT MOVEMENT!!  move() needs to go in the while true statement at the bottom
player.direction = ""


def go_up():
    if player.direction != "down":
        player.direction = "up"


def go_down():
    if player.direction != "up":
        player.direction = "down"


def go_left():
    if player.direction != "right":
        player.direction = "left"


def go_right():
    if player.direction != "left":
        player.direction = "right"


player_speed = .8


def move():
    global player_speed
    if player.direction == "up":
        y = player.ycor()
        player.sety(y + player_speed)

    if player.direction == "down":
        y = player.ycor()
        player.sety(y - player_speed)

    if player.direction == "left":
        x = player.xcor()
        player.setx(x - player_speed)

    if player.direction == "right":
        x = player.xcor()
        player.setx(x + player_speed)


def game_over_scr():
    global score

    pen.clear()
    pen.goto(0, 0)
    pen.write("GAME OVER\nSCORE: {}".format(score), align="center", font=("Courier", 60, "bold"))
    wn.bgcolor("red")

wn.listen()

wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

pen.write(score, align="center", font=("Courier", 30, "bold"))
max_ball = 0
game_ovr = 0
while game_ovr < 1:

    move()
    wn.update()



    # collision
    if player.distance(t1) < 20:
        t1.color("white")
        t1.goto(randint(-480, 480), randint(-380, 380))
        t1.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t2) < 20:
        t2.color("white")
        t2.goto(randint(-480, 480), randint(-380, 380))
        t2.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t3) < 20:
        t3.color("white")
        t3.goto(randint(-480, 480), randint(-380, 380))
        t3.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t4) < 20:
        t4.color("white")
        t4.goto(randint(-480, 480), randint(-380, 380))
        t4.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t5) < 20:
        t5.color("white")
        t5.goto(randint(-480, 480), randint(-380, 380))
        t5.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t6) < 20:
        t6.color("white")
        t6.goto(randint(-480, 480), randint(-380, 380))
        t6.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t7) < 20:
        t7.color("white")
        t7.goto(randint(-480, 480), randint(-380, 380))
        t7.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t8) < 20:
        t8.color("white")
        t8.goto(randint(-480, 480), randint(-380, 380))
        t8.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t9) < 20:
        t9.color("white")
        t9.goto(randint(-480, 480), randint(-380, 380))
        t9.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t10) < 20:
        t10.color("white")
        t10.goto(randint(-480, 480), randint(-380, 380))
        t10.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t11) < 20:
        t11.color("white")
        t11.goto(randint(-480, 480), randint(-380, 380))
        t11.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t12) < 20:
        t12.color("white")
        t12.goto(randint(-480, 480), randint(-380, 380))
        t12.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t13) < 20:
        t13.color("white")
        t13.goto(randint(-480, 480), randint(-380, 380))
        t13.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t14) < 20:
        t14.color("white")
        t14.goto(randint(-480, 480), randint(-380, 380))
        t14.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t15) < 20:
        t15.color("white")
        t15.goto(randint(-480, 480), randint(-380, 380))
        t15.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t16) < 20:
        t16.color("white")
        t16.goto(randint(-480, 480), randint(-380, 380))
        t16.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t17) < 20:
        t17.color("white")
        t17.goto(randint(-480, 480), randint(-380, 380))
        t17.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t18) < 20:
        t18.color("white")
        t18.goto(randint(-480, 480), randint(-380, 380))
        t18.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t19) < 20:
        t19.color("white")
        t19.goto(randint(-480, 480), randint(-380, 380))
        t19.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.distance(t20) < 20:
        t20.color("white")
        t20.goto(randint(-480, 480), randint(-380, 380))
        t20.color("black")
        player_speed += .1
        score += 1
        pen.clear()
        pen.write(score, align="center", font=("Courier", 30, "bold"))

    if player.ycor() > 390:
        wn.clearscreen()
        game_over_scr()
        game_ovr += 1
    if player.ycor() < -390:
        wn.clearscreen()
        game_over_scr()
        game_ovr += 1
    if player.xcor() > 490:
        wn.clearscreen()
        game_over_scr()
        game_ovr += 1
    if player.xcor() < -490:
        wn.clearscreen()
        game_over_scr()
        game_ovr += 1


turtle.mainloop()
