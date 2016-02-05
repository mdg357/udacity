#!/c/Users/User/Anaconda2/python

import webbrowser

class Movie():
    def __init__(self, title, storyline, poster_image, youtube_trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer_url

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)
