import turtle
from time import sleep
from random import randint

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+SPEED)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-SPEED)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+SPEED)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-SPEED)

def go_up():
    if head.direction == 'down':
        pass
    else:
        pen.clear()
        head.direction = 'up'

def go_down():
    if head.direction == 'up':
        pass
    else:
        pen.clear()
        head.direction = 'down'

def go_left():
    if head.direction == 'right':
        pass
    else:
        pen.clear()
        head.direction = 'left'

def go_right():
    if head.direction == 'left':
        pass
    else:
        pen.clear()
        head.direction = 'right'

if __name__ == '__main__':
    
    SPEED = 10

    try:
        segments = []

        sg = turtle.Screen()
        sg.title("Snake Game")
        sg.bgcolor("black")
        sg.setup(width=600, height=600)
        sg.tracer(0)

        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("circle")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0,250)

        pen.write("S N A K E  G A M E",align='center',font=('Comic San',25,'normal'))

        head = turtle.Turtle()
        head.speed(0)
        head.shape("circle")
        head.color("white")
        head.penup()
        head.goto(0,0)
        head.direction = 'stop'

        food = turtle.Turtle()
        food.speed(0)
        food.shape("circle")
        food.color("red")
        food.penup()
        food.goto(0,100)

        sg.listen()
        sg.onkeypress(go_up, 'Up')
        sg.onkeypress(go_down, 'Down')
        sg.onkeypress(go_left, 'Left')
        sg.onkeypress(go_right, 'Right')

        while True:
            sg.update() 

            if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
                sleep(1)
                head.goto(0,0)
                head.direction = 'stop'
                for segs in segments:
                    segs.goto(1920,1080)
                pen.write(f"YOUR FINAL SCORE WAS - {len(segments)}",align='center',font=("ZComic San",20,'normal'))
                segments.clear()
                SPEED = 10

            if head.distance(food) < 15:
                x = randint(-280,280)
                y = randint(-280,280)
                food.goto(x,y)
                SPEED += 0.2

                new_seg = turtle.Turtle()
                new_seg.speed(0)
                new_seg.shape("circle")
                new_seg.color("grey")
                new_seg.penup()
                segments.append(new_seg)

            for index in range(len(segments)-1,0,-1):
                x = segments[index-1].xcor()
                y = segments[index-1].ycor()
                segments[index].goto(x,y)

            if len(segments) > 0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x,y)
                    
            move()

            for seg in segments:
                if seg.distance(head) < 10:
                    sleep(1)
                    head.goto(0,0)
                    head.direction = 'stop'
                    for segs in segments:
                        segs.goto(1920,1080)
                    pen.write(f"YOUR FINAL SCORE WAS - {len(segments)}",align='center',font=("ZComic San",20,'normal'))
                    segments.clear()
                    SPEED = 10

            sleep(0.07)

        sg.mainloop()
    except:
        pass
