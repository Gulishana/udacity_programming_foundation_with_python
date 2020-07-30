import turtle

# build the function describing the repetitive movement
def draw_square(some_turtle):
    for i in range(1,5):   # range(1,5)=[1,2,3,4]
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    ################### Creat a window ##################
    window = turtle.Screen()
    window.bgcolor("red")

    ####### Create the turtle Brad - Draw a square #######
    brad = turtle.Turtle()  # grab out the Turtle function
    brad.shape("turtle")    # change the shape into a turtle
    brad.color("yellow")    # change the color to yellow
    brad.speed(2)           # change the speed to 2
    draw_square(brad)
    # use brad as the input variable of function draw_square:   brad=some_turtle

    ####### Create the turtle Angie - Draw a circle #######
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)  # radius = 100


    ################### Close the window ###############
    window.exitonclick()
    # close the window any time we click on it


# run the function
draw_art()


##################### Class ###########################
# Brad and Angie are the instances (or objects) of the class Turtle
