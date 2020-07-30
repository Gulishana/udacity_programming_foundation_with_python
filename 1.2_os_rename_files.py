# (1) Get all the file names
# (2) For each file: rename the file by removing all the numbers

import os    # os is short for "operating system"

# build the function
def rename_files():
    save_path = os.getcwd()
    # get the current working directory, and save the path
    print('Current working directory is', save_path)


    # (1) Part1: Get file names from a given folder
    file_list = os.listdir(r"D:\Udacity\Programming Foundation with Python\test")
    # get everything that's in a directory - files & directories
    # listdir() takes in the path of the folder
    # r stands for "rawpack", means to take this string as it is, and don't inperpret it in any other way
    # if not adding r, python will ignore \
    # there should be no space after r
    print('The files in the directory are:\n',file_list)


    os.chdir(r"D:\Udacity\Programming Foundation with Python\test")
    # change the working directory into the specified directory

    # (2) Part2: For each file, rename all filenames by removing numbers
    for file_name in file_list:
        deletechars = "0123456789"
        table = str.maketrans("", "", deletechars)
        # create a translation table
        # python3 requires the translate function to take in only one arugument (dict)
        new_name = file_name.translate(table)
        # str.translate function to remove chars in the string
        print('Old name:',file_name,'    New name:',new_name)

        os.rename(file_name,new_name)
        # rename the file, aruguments taken are (old_name, new_name)

    os.chdir(save_path)
    # change back to the original working directory



# run the function
rename_files()
