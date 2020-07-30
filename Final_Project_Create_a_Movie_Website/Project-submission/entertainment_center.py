# This file use class Movie that is built in 'media'
# And create objects/instances (some specific movie) from the class Movie

# It's good practice to keep the class definition in a separate file
# Then call and use the the class from another file

import media
import fresh_tomatoes_Youku

# instance:  self = eagle
         # Module.Class(Arguments/Variables)
         # these varialbes are Instance Variables, which are unique to each instance
cloud = media.Movie("Cloud Atlas",
                    "An epic science fiction film about six stories in different times.",
                    "https://upload.wikimedia.org/wikipedia/en/2/20/Cloud_Atlas_Poster.jpg",
                    "http://v.youku.com/v_show/id_XNDQ3NjMwNjU2.html?spm=a2h0j.8191423.chasing.1~3!10~A")
interstellar = media.Movie("Interstellar",
                    "An epic science fiction film directed by Nolan talking about wormhole.",
                    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                    "http://v.youku.com/v_show/id_XNzEzMDQ2NTM2.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")
pride = media.Movie("Pride & Prejudice (2005)",
                    "A love story in England, edited from Jane Austin's famous novel.",
                    "https://upload.wikimedia.org/wikipedia/en/0/03/Prideandprejudiceposter.jpg",
                    "http://v.youku.com/v_show/id_XMjg1NjI1OTkzMg==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2")
eagle = media.Movie("The Eagle Huntress",
                    "A 2016 Kazakn-language British-Mongolian-American documentary film.",
                    "https://upload.wikimedia.org/wikipedia/en/4/46/The_Eagle_Huntress.png",
                    "http://v.youku.com/v_show/id_XMTY4Mzc1OTg5Mg==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2")
geostorm = media.Movie("Geostorm",
                    "A series of extreme natural disasters caused by a satellite system Dutch Boy.",
                    "https://upload.wikimedia.org/wikipedia/en/7/76/Geostorm_official_teaser_poster.jpg",
                    "http://v.youku.com/v_show/id_XMzA1MTE0NDUxMg==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")
inception = media.Movie("Inception",
                    "The implantation of another person's idea into a target's subconscious.",
                    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                    "http://v.youku.com/v_show/id_XMTk0OTU5NDEy.html?spm=a2h0j.8191423.chasing.1~3!19~A")

# Print the Class Variable
# print (media.Movie.VALID_RATINGS)

# Print the pre-existing Class Variables
# print(media.Movie.__doc__)
# print(media.Movie.__name__)

# create a list or array of all the movies
movies = [cloud, interstellar, pride, eagle, geostorm, inception]

# call the function inside fresh_tomatoes_Youku to show the HTML page
fresh_tomatoes_Youku.open_movies_page(movies)
