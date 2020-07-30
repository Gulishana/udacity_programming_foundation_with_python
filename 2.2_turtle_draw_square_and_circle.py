import turtle

# build the function
def draw_square():
    ################### Creat a window ##################
    window = turtle.Screen()
    # create a window screen for Turtle to draw the shapes
    window.bgcolor("red")
    # background color of the window is red

    #################### Draw the square #################
    brad = turtle.Turtle()  # grab out the Turtle function
    brad.shape("turtle")    # change the shape into a turtle
    # there are shapes like "arrow", "turtle", "circle", "square", "triangle", "classic"
    brad.color("yellow")    # change the color to yellow
    brad.speed(2)           # change the speed to 2
    # the speed is limited to only integers within (1,10)

    brad.forward(100)
    # takes in a number, which is the distance we want to move forward
    brad.right(90)
    # takes in a number, which is the degee to turn right with

    # repeat 3 more times
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    ####### Create another turtle Angie - Draw a circle #######
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)  # radius = 100

    ################### Close the window ###############
    window.exitonclick()
    # close the window any time we click on it


# run the function
draw_square()


##################### Class ###########################
# Brad and Angie are the instances (or objects) of the class Turtle
