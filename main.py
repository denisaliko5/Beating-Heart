import turtle,math
t = turtle.Turtle()
t.ht()
t.color("red")
t.pensize(10)
t.speed(0)
a=90
a1=a*2+a/2
r=100
p=(0.375)*r*2*math.pi
t.pu()
t.goto(-r*4,r+20)
t.pd()
t.write("As a matter of fact, I'm so fucking deep in love with you! ;) <3",font=("Segoe UI",27,"normal"))
t.pu()
t.goto(0,0)
t.pd()
while True:
  for i in ["white","red"]:
    t.seth(a)
    t.color(i)
    t.begin_fill()
    t.circle(r,a1)
    t.fd(p)
    t.seth(-t.heading())
    t.fd(p)
    t.circle(r,a1)
    t.setpos(0,0)
    t.end_fill()