# Our Goal:
# 1) Read text
# 2) Check text for curse words

import urllib

# 1) Read text
def read_text():
    text = open(r"D:\Udacity\Programming Foundation with Python\test\curse_word.txt")
    # open is a built-in module in Python, which :
    # 1) takes in the address or the path of the file
    # 2) returns an object of the file type
    # r : takes the string as it is
    contents_of_file = text.read() # read the content of the file
    print(contents_of_file)
    text.close()  # close the file

    # check the profanity after reading the file content
    # so now we call the function below
    check_profanity(contents_of_file)

# 2) Check text for curse words using a website "http://www.wdyl.com/profanity?q"
def check_profanity(text_to_check):
    URL = "http://www.wdyl.com/profanity?q="
    connection = urllib.urlopen(URL+text_to_check)
    # urllib is a module that provides a high-level interface for fetching data across the WWW
    # function urlopen takes in an URL
    output = connection.read()
    # read a output response from the website
    print(output)
    # output format is : {"response": "false"}  or  {"response": "true"}
    connection.close()  # close the connection

    if "true" in output:
        print('Profanity Alert!')
    elif "false" in output:
        print('This document has no curse workds!')
    else:
        print('Could no scan the document properly.')


# run the function
read_text()

######################## Summary ############################
# Open a file:
# FileObject = open(FilePath)             # FileObject is an object of the file
# FileContent = FileObject.read()
# FileObject.close()

# Connect to a website:
# Connection = urllib.urlopen(URL)        # Connection is a file like object
# WebContent = Connection.read()
# Connection.close()
