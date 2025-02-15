import turtle

wn = turtle.Screen()

wn.title("PingPong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#P1

p_one = turtle.Turtle()
p_one.speed(0)
p_one.shape("square")
p_one.color("white")
p_one.shapesize(stretch_wid=5, stretch_len=1)
p_one.penup()
p_one.goto(-350,0)


#P2
p_two = turtle.Turtle()
p_two.speed(0)
p_two.shape("square")
p_two.color("white")
p_two.shapesize(stretch_wid=5, stretch_len=1)
p_two.penup()
p_two.goto(350,0)
#Ball

while True: 
    wn.update()
