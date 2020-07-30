import turtle

# build the function describing the repetitive movement
def draw_diamond(some_turtle):   # draw a diamond
    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.right(40)
        some_turtle.forward(100)
        some_turtle.right(140)


def draw_flower():
    ################### Creat a window ##################
    window = turtle.Screen()
    window.bgcolor("pink")  # change background to pink

    ####### Create the turtle Brad - Draw a square #######
    brad = turtle.Turtle()  # grab out the Turtle function
    brad.shape("turtle")    # change the shape into a turtle
    brad.color("red")       # change the color to red
    brad.speed(10)          # change the speed to 10

    for i in range(1,73):   # 360/5=72, thus turn right for 72 times
        draw_diamond(brad)
        brad.right(5)      # turn right by 5 degrees

    brad.right(90)
    # turtle start with forwarding right with a horizontal line
    # thus turn right 90 degrees to the vertical direction facing down
    brad.forward(300)

    ################### Close the window ###############
    window.exitonclick()
    # close the window any time we click on it


# run the function
draw_flower()


##################### Class ###########################
# Brad and Angie are the instances (or objects) of the class Turtle
