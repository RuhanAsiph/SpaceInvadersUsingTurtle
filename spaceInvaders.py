import turtle 
import math
import os
#set up the screen 
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
#add border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4): 
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

#create the main player turtle 
player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed=15

#create the enemy
enemy = turtle.Turtle()
enemy.color("blue")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2

#create player's weapon 
light = turtle.Turtle()
light.color("pink")
light.shape("triangle")
light.penup()
light.speed(0)
light.setheading(90)
light.shapesize(0.5,0.5)
light.hideturtle()

lightspeed = 20

#define light state 
#ready 
#fire
lightstate = "ready"

 




#move player left and right 
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x=-280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)
def emit():
	#Declare lightstate as a global variable
	global lightstate
	if lightstate == "ready":
		lightstate = "fire"
		#move light in front of the player 
		x = player.xcor()
		y = player.ycor() + 10 
		light.setposition(x,y)
		light.showturtle()
#t1 - turtle 1 
#t2 - turtle 2 
def isCollision(t1,t2):
	#using pythagorean theorem to check the distance between the enemies and the light 
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False

#interact with keyboard
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(emit, "space")

#Main gameloop
while True:
	#move the enemy 
	x = enemy.xcor()
	x += enemyspeed
	enemy.setx(x)
	#move the enemy back and down 
	if enemy.xcor() > 280:
		y = enemy.ycor()
		y -= 40
		enemyspeed *= -1
		enemy.sety(y)
	if enemy.xcor() < -280:
		y = enemy.ycor()
		y -= 40
		enemyspeed *= -1
		enemy.sety(y)
	#move the light 
	if lightstate == "fire":
		y = light.ycor()
		y +=  lightspeed
		light.sety(y)
	#check if the light has hit the border
	if light.ycor() > 275:
		light.hideturtle()
		lightstate = "ready"
	#check for a collision between light and the enemy 
	if isCollision(light, enemy):
		#Reset the light 
		light.hideturtle()
		lightstate = "ready"
		light.setposition(0,-400)
		#Reset the enemy 
		enemy.setposition(-200,250)
	#check for a collision between the player and the enemy 
	if isCollision(player, enemy):
		player.hideturtle()
		enemy.hideturtle()
		print("Game Over")
		break;









wn.mainloop()