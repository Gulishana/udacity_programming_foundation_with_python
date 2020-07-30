# class Parent:
    # --last_name   --eye_color
    # function : show_info()
# class Child:
    # --number_of_toys  ## Other variables inherits from class Parent
    # function also inherits form class Parent

class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print('Last Name :', self.last_name)
        print('Eye Color :', self.eye_color)


jacky_chen = Parent("Chen","black")
jacky_chen.show_info()             # call the function


# Class Child inherits or reuses everything that is publicly available in Class Parent
# This inludes BOTH the Instance Variables AND the Instance Methods
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
        # NO NEED TO DO ANYTHING WITH THE INSTANCE FUNCTION IF WE WANT TO USE THE SAME FUNCTION


miley_cyrus = Child("Cyrus","Blue", 5)
miley_cyrus.show_info()          # call the inherited function from Parent


############################## Method Overriding ################################
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    # IF WE DEFINE THE FUNCITON WITH SAME NAME AGAIN, THEN ONLY THE CURRENT FUNCTION WILL BE CALLED
    # IN THIS WAY, OVERRIDE THE PARENT METHOD !!!
    def show_info(self):
        print('Last Name :', self.last_name)
        print('Eye Color :', self.eye_color)
        print('Number of Toys :', str(number_of_toys))


miley_cyrus = Child("Cyrus","Blue", 5)
miley_cyrus.show_info()          # call the funciton defined in the class Child
