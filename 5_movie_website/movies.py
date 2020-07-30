# This file use class Movie that is built in 'media'
# And create objects/instances (some specific movie) from the class Movie

# It's good practice to keep the class definition in a separate file
# Then call and use the the class from another file

import class_Movie
import website_design_HTML

# instance:  self = toy_story
         # Module.Class(Arguments/Variables)
         # these varialbes are Instance Variables, which are unique to each instance
toy_story = class_Movie.Movie("Toy Story",
                              "A story of a boy and his toys that come to life",
                              "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                              "http://my.tv.sohu.com/us/63327699/64241398.shtml")
                              # original website at YouTube:
                              # https://www.youtube.com/watch?v=vwyZH85NQC4
#print(toy_story.storyline)
#toy_story.show_trailer()   # call the Intance Method defined inside the class


# instance:  self = avatar
avatar = class_Movie.Movie("Avatar",
                           "A marine on an alien planet",
                           "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                           "http://www.iqiyi.com/w_19rtepe9ll.html")
                           # original website at YouTube:
                           # http://www.youtube.com/watch?v=-9ceBgWV8io
#print(avatar.storyline)
#avatar.show_trailer()     # call the Intance Method defined inside the class

pride = class_Movie.Movie("Pride & Prejudice",
                     "A love story in England, edited from Jane Austin's famous novel",
                     "https://upload.wikimedia.org/wikipedia/en/0/03/Prideandprejudiceposter.jpg",
                     "http://www.iqiyi.com/w_19rsoe2u59.html")
inception = class_Movie.Movie("Inception",
                     "The implantation of another person's idea into a target's subconscious",
                     "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                     "http://www.iqiyi.com/w_19rs6mvhuh.html")
interstellar = class_Movie.Movie("Interstellar",
                     "A 2014 epic science fiction film directed by Nolan talking about wormhole",
                     "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                     "http://my.tv.sohu.com/us/179009704/72185222.shtml")
geostorm = class_Movie.Movie("Geostorm",
                     "A series of extreme natural disasters caused by a satellite system Dutch Boy",
                     "https://upload.wikimedia.org/wikipedia/en/7/76/Geostorm_official_teaser_poster.jpg",
                     "http://www.iqiyi.com/w_19rvcirgy9.html")

# print the Class Variable
print (class_Movie.Movie.VALID_RATINGS)
# print the pre-existing Class Variables
print(class_Movie.Movie.__doc__)
print(class_Movie.Movie.__name__)
print(class_Movie.__module__)


# create a list or array of all the movies
movies = [toy_story, avatar, pride, inception, interstellar, geostrom]

# call the function inside build_website to show the HTML page
website_design_HTML.open_movies_page(movies)
