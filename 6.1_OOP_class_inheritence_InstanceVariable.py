# class Parent:
    # --last_name   --eye_color
# class Child:
    # --number_of_toys  ## Other variables inherits from class Parent

class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

# build an Instance of Class Parent
jacky_chen = Parent("Chen","black")
# here we did not call the Class the file name first
# since we are now within the same file for ease of demonstration
print(jacky_chen.last_name)


# Class Child inherits or reuses everything that is publicly available in Class Parent
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        # initialize the Instance Variables inherited from Class Parent by reusing __init__ inside Parent
        Parent.__init__(self, last_name, eye_color)
        # initialize uqinue Instance Variable for the current class
        self.number_of_toys = number_of_toys

# build an Instance of Class Child
miley_cyrus = Child("Cyrus","Blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)
