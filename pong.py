import turtle
import winsound
# screen setup
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Sdore
scoreA = 0
scoreB = 0
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(10)  # speed of animation
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("blue")
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(10)  # speed of animation
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(100)  # speed of animation
ball.shape("circle")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.color("white")
ball.penup()
ball.goto(0, 0)
# everytime ball move, move by 2 pixel
ball.dx = 0.7
ball.dy = 0.7

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {scoreA} Player B: {scoreB}", align="center",
          font=("Courier", 24, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()  # from turtle module
    y += 60
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # from turtle module
    y -= 60
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # from turtle module
    y += 60
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # from turtle module
    y -= 60
    paddle_b.sety(y)


# keyboard binding
wn.listen()  # for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball respond to the corner
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -0.8
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -0.8
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        # ball.goto(0, 0)
        ball.setx(390)
        ball.dx *= -0.8
        scoreA += 1  # add player A score
        pen.clear()
        pen.write(f"Player A: {scoreA} Player B: {scoreB}", align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        # ball.goto(0, 0)
        ball.setx(-390)
        ball.dx *= -0.8
        scoreB += 1  # add palyer B score
        pen.clear()
        pen.write(f"Player A: {scoreA} Player B: {scoreB}", align="center",
                  font=("Courier", 24, "normal"))

    # ball and paddle collide
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -0.8
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -0.8
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
