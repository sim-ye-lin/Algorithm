import turtle as t
t.shape("turtle")

def up():
    t.setheading(90)
    t.forward(10)
def down():
    t.setheading(270)
    t.forward(10)
def right():
    t.setheading(0)
    t.forward(10)
def left():
    t.setheading(180)
    t.forward(10)
def key_r():
    t.clear()
    t.penup()
    t.goto(0,0)
    t.pendown()
    
s = t.Screen()
s.onkey(up, "Up")
s.onkey(down, "Down")
s.onkey(right, "Right")
s.onkey(left, "Left")
s.onkey(key_r, "r")
s.listen()
