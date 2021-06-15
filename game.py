import turtle
import time
import random
import math

# parmanent variables
WIDTH = 500
HEIGHT = 500
dx = -3
dy = -3
i=0
j=0 
codx = -255
cody = 200
score_player = 0
COLOR = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black','gray', 'white']


#setting up working space 
window = turtle.Screen()
window.title('Bounching Ball')
window.bgpic('C:\\Users\\royel\\djangoAdvance\\arc\\bg_pic2.png')
window.setup(WIDTH,HEIGHT)
window.tracer(0)

#boder
box = turtle.Turtle()
box.hideturtle()
box.color('black')
box.width(3)
box.penup()
box.right(90)
box.goto(0,-250)
box.pendown()
box.left(90)
box.forward(250)
box.left(90)
box.forward(500)
box.left(90)
box.forward(500)
box.left(90)
box.forward(500)
box.left(90)
box.forward(250)


#ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('#0a4c03')
ball.penup()
ball.goto(0,-216)

#bubble 
no_of_bubbles = 80
bubbles = []

#creating multiple turtle for bubble
while i != no_of_bubbles:
    bubbles.append(turtle.Turtle())
    i+=1
i=0

#setting bubble position
while i!=no_of_bubbles:
    buble = bubbles[i]
    if j == 16:
        codx = -255
        cody = cody - 30
        j=1
    else:
        j+=1       
    buble.shape('circle')
    col = random.choice(COLOR)
    buble.color(col)
    buble.penup()
    codx += 30
    buble.goto(codx,cody)
    i+=1
    time.sleep(0)

#bat
bat = turtle.Turtle()
bat.shape('square')
bat.color('#800080')
bat.penup()
bat.shapesize(stretch_len=6,stretch_wid=1.5)
bat.goto(0,-245)

#bat function
def left():
    x=bat.xcor()
    bat.setx(x-20)


def right():
    x = bat.xcor()
    bat.setx(x+20)

#ball movement 
def movement():
    ball.goto(ball.xcor()+dx,ball.ycor()+dy)    

#Game over
def game_over():
    window.clear()
    game = turtle.Turtle()
    game.hideturtle()
    game.write('Game Over', font=('arial', 50), align='center')
    time.sleep(1)

#removing ball when collide wirh ball 
def Collision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False  

#score board
score = turtle.Turtle()
score.hideturtle()
score.penup()
score.speed(0)
score.color('#A32CC4')
score.goto(0,220)
score.write('Score: {}'.format(score_player),font=('arial',15),align= 'center')

#score border
score_border = turtle.Turtle()
score_border.hideturtle()
score_border.color('black')
score_border.width(3)
score_border.left(90)
score_border.penup()
score_border.forward(215)
score_border.pendown()
score_border.left(90)
score_border.forward(248)
score_border.right(90)
score_border.forward(33)
score_border.right(90)
score_border.forward(488)
score_border.right(90)
score_border.forward(33)
score_border.right(90)
score_border.forward(248)

#on key press
window.listen()
window.onkeypress(left,'Left')
window.onkeypress(right,'Right')


#main function
while True:
    movement()

    #ball return when strick on border 
    if ball.xcor() >= 240:
        dx*=-1
    if ball.xcor() <= -240:
        dx*=-1      
    if ball.ycor() >= 200:
        dy*=-1

    #bat cannot go further then border 
    if bat.xcor() <= -190:
        bat.setx(-190)
    if bat.xcor() >= 190:
        bat.setx(190)   

    #game over when ball misses to hit ball    
    if ball.ycor() <= -250:
        game_over()

    #when bat hits the ball    
    if (ball.ycor() <= -220) and (ball.xcor()>bat.xcor()-60 and ball.xcor()<bat.xcor()+60):
        ball.sety(-220)
        dy *= -1 

    #bubble popping function
    for bubble in bubbles:
        if Collision(ball,bubble):
            dy *= -1 
            bubble.goto(550,550)
            bubble.hideturtle()
            score_player += 1
            score.clear()
            score.write('Score: {}'.format(score_player), font=('arial', 15), align='center')
            time.sleep(0)


    window.update()