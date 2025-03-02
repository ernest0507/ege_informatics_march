from turtle import *

screensize(1500, 1500)
tracer(0)
lt(90)
k = 35

rt(60)
for _ in range(2):
    fd(7 * k)
    rt(120)

rt(300)
fd(7 * k)

for _ in range(2):
    rt(60)
    fd(7 * k)
    rt(60)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')

exitonclick()
# Ответ: 66
