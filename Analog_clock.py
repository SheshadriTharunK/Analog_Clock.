from turtle import Turtle, Screen
import datetime

window = Screen()
window.title("Analog Digital Clock")
window.bgcolor("black")
window.setup(width=1000, height=800)

circle = Turtle()
circle.penup()
circle.pencolor("#118893")
circle.speed(0)
circle.pensize(25)
circle.hideturtle()
circle.goto(0, -390)
circle.pendown()
circle.fillcolor("#17202A")
circle.begin_fill()
circle.circle(400)
circle.end_fill()

hHand = Turtle()
hHand.shape("arrow")
hHand.color("white")
hHand.speed(10)
hHand.shapesize(stretch_wid=0.4, stretch_len=18)

mHand = Turtle()
mHand.shape("arrow")
mHand.color("white")
mHand.speed(10)
mHand.shapesize(stretch_wid=0.4, stretch_len=26)

sHand = Turtle()
sHand.shape("arrow")
sHand.color("dark red")
sHand.speed(10)
sHand.shapesize(stretch_wid=0.4, stretch_len=36)

centerCircle = Turtle()
centerCircle.shape("circle")
centerCircle.color("white")
centerCircle.shapesize(stretch_wid=1.5, stretch_len=1.5)

pen = Turtle()
pen.speed(0)
pen.color("white")

hour_positions = [(-20, 180), (-20, 170), (-20, 160)]
minute_positions = [(-20, 90), (-20, 80), (-20, 70)]
second_positions = [(-20, 40), (-20, 30), (-20, 20)]

for pos in hour_positions:
    pen.penup()
    pen.hideturtle()
    pen.goto(pos)
    pen.write("1", align="center", font=("Algerian", 20, "bold"))

for pos in minute_positions:
    pen.penup()
    pen.hideturtle()
    pen.goto(pos)
    pen.write("1", align="center", font=("Algerian", 20, "bold"))

for pos in second_positions:
    pen.penup()
    pen.hideturtle()
    pen.goto(pos)
    pen.write("1", align="center", font=("Algerian", 20, "bold"))

def move_h_hand():
    current_hour_internal = datetime.datetime.now().hour
    degree = (current_hour_internal - 15) * -30
    current_minute_internal = datetime.datetime.now().minute
    degree = degree + (-0.5 * current_minute_internal)
    hHand.setheading(degree)
    window.ontimer(move_h_hand, 60000)

def move_m_hand():
    current_minute_internal = datetime.datetime.now().minute
    degree = (current_minute_internal - 15) * -6
    current_second_internal = datetime.datetime.now().second
    degree = degree + (-current_second_internal * 0.1)
    mHand.setheading(degree)
    window.ontimer(move_m_hand, 1000)

def move_s_hand():
    current_second_internal = datetime.datetime.now().second
    degree = (current_second_internal - 15) * -6
    sHand.setheading(degree)
    window.ontimer(move_s_hand, 1000)

window.ontimer(move_h_hand, 1)
window.ontimer(move_m_hand, 1)
window.ontimer(move_s_hand, 1)

window.exitonclick()
