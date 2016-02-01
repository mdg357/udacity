#!/c/Python27/python
import re
from os.path import join
from os import getcwd

# Read text from a document
def read_text(filePath, fileName):
    quotes = open(join(filePath, fileName), "r")
    contentsOfFile = quotes.read()
    quotes.close()
    
    return contentsOfFile

def clean_word(word):
    word = word.strip(",()-.").lower()
    regex = re.compile('[^a-z]')
    regex.sub('', word)
    print word
    return word

def get_word_list(lines):
    wordList = []

    for word in lines.split():
        wordList.append(clean_word(word))
        
    return wordList

# Check for profanity
fileContents = read_text(getcwd(), "movie_quotes.txt")
profanity = read_text(getcwd(), "profanity.txt")
messageWords = get_word_list(fileContents)
curseWords = get_word_list(profanity)
