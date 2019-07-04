import turtle

window = turtle.Screen() # create a pop up window
window.setup(width=800, height=600, startx=10, starty=0.5) # scaling the window
joe = turtle.Turtle() # the turtle object. names is joe
joe.shape('turtle')
scale = 5
joe.speed(10)

# where joe will start
joe.penup()
joe.setpos(-390, 0)
joe.pendown()

current = 0 # location of where joe is
seen = set() # keeping track of where joe has been

# the commands for joe
for step_size in range(1,100): # joe increases step by 1 each time

    backwards = current - step_size

    if backwards > 0 and backwards not in seen:
        joe.setheading(90) # 90 degrees is pointing straight up
        joe.circle(scale * step_size/2, 180) # 180 degrees means 'draw semicircle'
        current = backwards
        seen.add(current)

    else:
        joe.setheading(270) # 270 degrees is straight down
        joe.circle(scale * step_size/2, 180)
        current += step_size
        seen.add(current)

turtle.done() # this keeps the window open after joe is done

'''
    # code for linear movement
    # step backwards if its positive and joe has never been there before
    if backwards > 0 and backwards not in seen:
        joe.backward(step_size)
        current = backwards
        seen.add(current)

    # otherwise, go forward
    else:
        joe.forward(step_size)
        current += step_size
        seen.add(current)
'''