#!/c/Python27/python
import urllib
from os.path import join
from os import getcwd

# Read text from a document
def read_text(filePath, fileName):
    fileHandle = open(join(filePath, fileName), "r")
    contentsOfFile = fileHandle.read()
    fileHandle.close()    
    return contentsOfFile

def check_for_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    connection.close()
    return output

def check_response(response):
    if("true" in response):
        print "Profanity alert!"
    elif("false" in response):
        print "No profanity found in text."
    else:
        print "Unable to determine response."

# Check for profanity
fileContents = read_text(getcwd(), "movie_quotes.txt")
response = check_for_profanity(fileContents)
check_response(response)
