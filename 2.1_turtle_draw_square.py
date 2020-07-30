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

    ################### Close the window ###############
    window.exitonclick()
    # close the window any time we click on it


# run the function
draw_square()


##################### Class ###########################
# turtle is one of the file in the Python standard library,
# turtle.Turtle is a subclass in that files
# tuttle.Turtle() calls a function in the Turtle class:   def__init__
#      def__init__ is defined inside the class turtle, and it creates space in memory
#      for a new instance or a new object of the class Turtle.
#      This instance we called "brad" here.
# "brad" can then access all of the rest of the methods that are inside the class Turtle
