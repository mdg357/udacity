import re

# Read text from a document
def read_text():
    quotes = open("C:/Users/User/Documents/Git/udacity/Programming Foundations with Python/movie_quotes.txt", "r")
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

fileContents = read_text()
words = get_word_list(fileContents)
