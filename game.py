import turtle
import time
import random
import math

# parmanent variables
WIDTH = 500
HEIGHT = 500
dx = 3
dy = 3
i=0
j=0 
codx = -255
cody = 230
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
while i!=112:
    if j == 16:
        codx = -255
        cody = cody - 30
        j=1
    else:
        j+=1       
    bubble = turtle.Turtle()
    bubble.shape('circle')
    col = random.choice(COLOR)
    bubble.color(col)
    bubble.penup()
    codx += 30
    bubble.goto(codx,cody)
    i+=1

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
     
# def move():
#     if True == a:
#         x=bat.xcor()
#         bat.setx(x-1)
#     else:
#         x = bat.xcor()
#         bat.setx(x+1)


#ball movement 
def movement():
    ball.goto(ball.xcor()+dx,ball.ycor()+dy)    

#Game over
def game_over():
    window.clear()
    game = turtle.Turtle()
    game.hideturtle()
    game.write('Game Over', font=('arial', 50), align='center')
    time.sleep(3)

def Collision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 20:
        return True
    else:
        return False    


#on key press
window.listen()
window.onkeypress(left,'Left')
window.onkeypress(right,'Right')



while True:
    movement()
    #move()

    #ball return when strick at border 
    if ball.xcor() >= 250:
        dx*=-1
    if ball.xcor() <= -250:
        dx*=-1      
    if ball.ycor() >= 250:
        dy*=-1

    #bat stop when it     
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

    if Collision(ball,bubble):
        ball.sety(10)
        dy *= -1 
        bubble.hideturtle()

    window.update()