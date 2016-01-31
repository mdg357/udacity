from os import listdir, rename
from os.path import isfile, join

# Functions

def remove_numbers_from_string(string):
    return string.translate(None, "0123456789")

def rename_files(folderPath, filename):
    newFilename = remove_numbers_from_string(filename)
    rename(join(folderPath, filename), join(folderPath, newFilename))
    print "Renaming '{0}' to '{1}'".format(filename, newFilename) 
    
# Settings

folderPath = 'C:/Users/User/Documents/Git/udacity/Programming Foundations with Python/prank'
onlyfiles = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]

# Loop through the files
for file in onlyfiles:
    rename_files(folderPath, file)