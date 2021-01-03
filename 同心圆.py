import turtle
turtle.setup(650,450)
turtle.color('blue')
for n in range(1,5):
    r=50*n
    turtle.circle(r,360)
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(50)
    turtle.seth(0)
    turtle.pendown()
turtle.size(10)#如何终止程序？


