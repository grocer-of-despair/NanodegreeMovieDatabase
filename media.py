import webbrowser

class Movie():
    # Defining __doc__ (""" allows you to use multiple lines """)
    """ This class provides a way to store movie related information """

    #Class VARIABLE. If the variable is not going to change then use ALL_CAPS
    VALID_RATINGS = ["G","PG","PG-13","R"]

    #Class CONSTRUCTOR
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # Instance VARIABLES
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #An Instance Method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
