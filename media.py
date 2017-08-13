import webbrowser
import imdb

class Movie():
    """ This class provides a way to store movie related information """

    # Class CONSTRUCTOR
    def __init__(self, movie_title, poster_image, trailer_youtube, imdb_link):

        # Instance VARIABLES
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.link = imdb_link

    # When the movie tile is clicked this creates a modal to show the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    # This uses the IMDB API to search for Movie Data
    def imdb_info(self):

        # Create instance of IMDB Class
        ia = imdb.IMDb()

        # Use the Instance Title to search IMDB
        title = self.title
        s_result = ia.search_movie(title)
        movie = s_result[0] # Take the first result
        ia.update(movie) # Update the class instance to the IMDB search Result

        """ Pulls the data required for the movie from IMDB
        In the case of a key having multiple results i.e. Director, Plot, we take the first result
        and assign it to variables
        """
        director = movie['director'] # Get
        self.director = director[0]
        plot = movie['plot']
        self.plot = plot[0]
        actors = movie['cast']
        self.rating = movie['rating']
