# This file defines the class Movie
# coding = UTF-8 (for better communication)

# class Movie :
# 1) Things to remember:
#    --title   --storyline  --poster_image  --youku_trailer [URL link]
# 2) Things to do:
#    --show_trailer()  function to show the URL link

import webbrowser

class Movie():
    '''This class provides a way to store movie related information'''
    # use triple quotes to define the Class

    VALID_RATINGS = ["G","PG","PG-13","R"]    # Class Variable, a constant

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
    # self is the object/Instance being created (Default in Python)
    # other 4 are the informations that __init__ function takes in as arguments
    # and we need to initializes following Instance Variables for Instance self
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# without "self." before the Instance Variables,
# then it becomes a simple Local Variable inside funciton __init__

    def show_trailer(self):      # an Instance Method
        webbrowser.open(self.trailer_youtube_url)



################################ Summary #######################################
# VALID_RATINGS:
    # Class Variable outside the init function
    # this varibale will be shared by all the instances created by this Class
    # it is like a Constant
# pre-existing Class Variables:
    # __doc__ :  gives some documentation of the Class
    # __name__
    # __module__
# __init__ :
    # function init initializes or creates space and memory for a new Instance
    # init is also called a Class Constructor
    # init initializes all the data associated with the Instance
    # "__" on both sides shows that name init is essentially reserved in Python,
    # and it is a special function or method
    # once Class Movie is called, the constructor function  __init__  is called
    # init function takes in arguments:
        # the first argument must by Instance "self"
        # and the others are Instance Variables
# self:
    # self is the new object/Instance bejing created from Class Movie
    # self is the default for an Instance in Python
# show_trailer(self):
    # function that is defined inside a Class and is associated with an Instance
    # is called an Instance Method
    # the first arugument for an Instance Method must be the Instance "self"
