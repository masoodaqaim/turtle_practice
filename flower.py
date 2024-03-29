from turtle import Turtle, Screen


def draw_square(some_turtle):
    for _ in range(4):
        some_turtle.forward(200)
        some_turtle.right(90)


def draw_art():
    # Turtle Brad
    brad = Turtle(shape="turtle")
    brad.color("blue")
    brad.pensize(2)
    # brad.speed("normal")  # 6/normal is the default so don't need to do it
    brad.speed(0)

    for _ in range(36):
        draw_square(brad)
        brad.right(10)

    # Turtle Angie
    angie = Turtle(shape="turtle")
    angie.color("red")
    angie.pensize(2)
    # angie.speed(5)  # slightly slower than brad
    angie.speed(0)

    size = 1

    for _ in range(300):
        angie.forward(size)
        angie.right(91)
        size += 1


window = Screen()
window.bgcolor("black")

draw_art()

window.exitonclick()
