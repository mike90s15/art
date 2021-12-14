#!/usr/bin/env bash
import turtle

a=0
b= 0

turtle.bgcolor('black')
turtle.speed(100)
turtle.pen(fillcolor='cyan', pencolor='green')

while True:
    turtle.forward(250)
    turtle.left(170)
    a += 1
	
    if a == 72:
        a = 0
	break
		
turtle.home()
turtle.pen(pencolor='black')
turtle.right(180)
turtle.forward(10)
turtle.pen(pencolor='cyan')

while True:
    turtle.forward(250)
    turtle.right(170)
    a += 1	
    if a == 9:
        turtle.pen(pencolor='blue')
    if a == 18:
        turtle.pen(pencolor='green')
    if a == 36: #36
        turtle.pen(pencolor='cyan')
    if a == 54:
        turtle.pen(pencolor='blue')
    if a == 72:
	turtle.done()
