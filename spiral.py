import turtle

colors = ['red', 'blue', 'green', 'yellow']

window = turtle.Screen() # create a pop up window
window.setup(width=800, height=600, startx=10, starty=0.5) # scaling the window
turtle.bgcolor('black')
joe = turtle.Turtle() # the turtle object. names is joe
joe.shape('turtle')
scale = 5
joe.speed(0)

# this creates a spiral. joe goes forward by 1 step, then rotates left by 59 degrees 
for x in range(360):
    joe.pencolor(colors[x % 4]) # for each line, a new color will be used
    joe.forward(x)
    joe.left(59)

turtle.done()  # this keeps the window open after joe is done
