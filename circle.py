import turtle

window = turtle.Screen() # create a pop up window
window.setup(width=800, height=600, startx=10, starty=0.5) # scaling the window
turtle.bgcolor('black') # background color, not sure why it says 'cannot find reference to bgcolor'
joe = turtle.Turtle() # the turtle object. names is joe
joe.shape('turtle')
scale = 5
joe.speed(0) # 0 is the fastest

for x in range(50):
    joe.pencolor('blue')
    joe.circle(100)
    joe.pencolor('red')
    joe.circle(50)
    joe.left(360/50)
    joe.pencolor('yellow')
    joe.circle(25)

turtle.done()