import turtle
import time
import random
import math
import winsound

#permanent variables
WIDTH = 500
HEIGHT = 500
dx = 3.5
dy = 3.5
i=0
j=0
COUNT = 0
#use for setting position of bubble
codx = -255
cody = 200
score_player = 0
COLOR = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown','gray', 'white']

#path for img file
loading = ".\\Loading\\"
end = ".\\Coffin_Dance\\"

#setting up working space
window = turtle.Screen()
window.title('Bounching Ball')
window.setup(WIDTH,HEIGHT)

#loading_frame
def loading_frame():
    image_no = 1
    img_no = 1
    img_no1 = 1
    winsound.PlaySound('voice.wav',winsound.SND_ASYNC)
    #team image 
    while img_no <= 20:
        im = str(image_no)
        window.addshape(loading + im + '.gif')
        time.sleep(0.01)
        load.shape(loading + im + '.gif')
        img_no += 1
    time.sleep(1.99)
    winsound.PlaySound('bgmusic.wav',winsound.SND_ASYNC)    

    #loading image
    while image_no <=68:
        img = str(image_no)
        window.addshape(loading + '\\loading' + img + '.gif')
        time.sleep(0.01)
        load.shape(loading + '\\loading' + img + '.gif')
        image_no += 1

    #instruction
    while img_no1 <=5:
        img = str(img_no1)
        window.addshape(loading + '\\game_instruction' + img + '.gif')
        time.sleep(0.8)
        load.shape(loading + '\\game_instruction' + img + '.gif')
        img_no1 += 1

#turtle for loading frame
load = turtle.Turtle()
loading_frame()
window.tracer(0)


#boder
box = turtle.Turtle()
box.color('Black')
box.width(5)
box.penup()
box.speed(0)
box.setposition(-250,250)
box.pendown()
for border in range(4):
    box.fd(500)
    box.right(90)
    box.fd(500)
    box.right(90)
box.hideturtle()

# Score border
box = turtle.Turtle()
box.hideturtle()
box.color('white')
box.penup()
box.speed(0)
box.setposition(-247,245)
box.pendown()
box.pensize(3)
for border in range(4):
    box.fd(487)
    box.right(90)
    box.fd(30)
    box.right(90)
box.hideturtle()

#ball
ball = turtle.Turtle()
ball.shape('circle')
col = random.choice(COLOR)
ball.color(col)
ball.penup()
ball.goto(0,-216)

#bubble decleration
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
    bat.setx(x-30)

def right():
    x = bat.xcor()
    bat.setx(x+30)

#ball movement
def movement():
    ball.goto(ball.xcor()+dx,ball.ycor()+dy)


#Game over
def game_over():
    window.clear()
    game = turtle.Turtle()
    window.bgcolor('#8AC8FD')
    image_no = 1
    winsound.PlaySound('Coffin_Dance_audio.wav',winsound.SND_ASYNC)
    #used for coffin dance img
    while image_no <=80:
        img = str(image_no)
        window.addshape(end + '\\Cofine_Dance' + img + '.gif')
        time.sleep(0.0001)
        game.shape(end + '\\Cofine_Dance' + img + '.gif')
        image_no += 1  
    game.hideturtle()
    game.write('****GAME OVER****\n\n\n\n\n   Your score is: {} '.format(COUNT),game.color('red'), font=('arial', 20), align='center')
    time.sleep(3)
    
#winner   
def winner():
    window.clear()
    winner = turtle.Turtle()

    winner.hideturtle()
    winner.write('You Win(:\n\n\n\n\n    Your score is: {} '.format(COUNT),winner.color('Green'), font=('arial', 20), align='center')
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
score.color('white')
score.goto(0,220)
score.write('Score: {}'.format(score_player),font=('arial',15),align= 'center')


#on key press
window.listen()
window.onkeypress(left,'Left')
window.onkeypress(right,'Right')

#main function
while True:
    #ball movement function calling
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
        break

    #when bat hits the ball
    if (ball.ycor() <= -220) and (ball.xcor()>bat.xcor()-60 and ball.xcor()<bat.xcor()+60):
        winsound.PlaySound('hit.wav',winsound.SND_ASYNC)
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
            winsound.PlaySound('pop.wav',winsound.SND_ASYNC)
            score.write('Score: {}'.format(score_player), font=('arial', 15), align='center')
            time.sleep(0)
            COUNT += 1
            if COUNT == no_of_bubbles:
               winner()

    window.update()