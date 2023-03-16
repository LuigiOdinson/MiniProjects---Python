import turtle
from random import randrange
from math import sqrt
wn = turtle.Screen()
wn.title("Fruit Catch")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)
score = 0

# text
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("courier", 20, "normal"))

# paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# fruit
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("red")
fruit.penup()
fruit.goto(randrange(-380, 380), 300)
fruit.dy = -0.06

# functions
def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)

# keyboard input
wn.listen()
wn.onkeypress(paddle_right, "d")
wn.onkeypress(paddle_left, "a")

# main
while True:
    wn.update()
    # fruit movement
    fruit.sety(fruit.ycor() + fruit.dy)
    # fruit catch check
    distance = sqrt((fruit.xcor() - paddle.xcor())**2 + (fruit.ycor() - paddle.ycor())**2)
    fruit_radius = 10
    paddle_radius = sqrt(2600)
    paddle_touched = False
    if distance < fruit_radius + paddle_radius:
        print("Collision")
        score += 5
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("courier", 20, "normal"))
        paddle_touched = True
        fruit.goto(randrange(-380, 380), 300)
    if fruit.ycor() < -280:
        if not paddle_touched:
            pen.clear()
            pen.goto(0, 0)
            pen.color("blue")
            pen.write("You scored {} points\n   click to exit".format(score), align="center", font=("courier", 20, "normal"))
            turtle.exitonclick()
    # paddle border check
    if paddle.xcor() > 350:
        paddle.setx(-350)
    if paddle.xcor() < -350:
        paddle.setx(350)
