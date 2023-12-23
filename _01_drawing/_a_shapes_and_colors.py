import turtle

if __name__ == '__main__':
    window=turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    jeffery  = turtle.Turtle()

    # Make your turtle's shape 'turtle',jeffery .shape('turtle')
    jeffery.shape ('turtle')
    # Set your turtle's speed using .speed(2)
    jeffery.speed(2)

    # Set your turtle's color using .color('green') and .pencolor('blue')
    jeffery.color('green')
    jeffery.pencolor ('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    jeffery.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    jeffery.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    for i in range(4):
        jeffery.forward(100)
        jeffery.left(90)

    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    jeffery.goto(7,8)
    # x=0 and y=0 is the center of the screen

    # Have your turtle draw a circle using .circle(radius, steps=30)
    jeffery.circle(radius=100, steps=65)
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    jeffery.begin_fill()
    jeffery.circle(radius=60, steps=98)
    jeffery.end_fill()
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors
    jeffery.begin_fill()
    jeffery.triangle(radius=77,steps=76)
    jeffery.end_fill()
    jeffery.begin_fill()
    jeffery.star(radius=88,steps=56)
    jeffery.end_fill()
    jeffery.begin_fill()


    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
