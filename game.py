import turtle
import time

# parmanent variables
WIDTH = 500
HEIGHT = 500
dx = 2
dy = 2


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
    bat.setx(x+1)
     
# def move():
#     if a == 1:
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

#on key press
window.listen()
window.onkeypress(left,'Left')
window.onkeypress(right,'Right')



while True:
    movement()
    # move()


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
              
    window.update()