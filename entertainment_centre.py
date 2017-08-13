#!/usr/bin/env python2
import media # Contains the Movie Class Constructor
import fresh_tomatoes # Creates the HTML Document

""" Creates a class instance for each Movie

Args:
    movie_title: The title of the movie, also used to search IMDB
    poster_image: The Wikimedia Movie Poster link
    trailer_youtube: A link to the Trailer on youtube
    imdb_link: A link to the movie's IMDB Webpage
"""

seven = media.Movie("Seven",
                    "https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg",
                    "https://www.youtube.com/watch?v=znmZoVkCjpI",
                    "https://www.imdb.com/title/tt0114369/?ref_=fn_al_tt_1")

fight_club = media.Movie("Fight Club",
                    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                    "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                    "https://www.imdb.com/title/tt0137523/?ref_=nv_sr_1")

last_samurai = media.Movie("The Last Samurai",
                    "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Last_Samurai.jpg",
                    "https://www.youtube.com/watch?v=T50_qHEOahQ",
                    "https://www.imdb.com/title/tt0325710/?ref_=nv_sr_1")

hard_to_kill = media.Movie("Hard To Kill",
                    "https://upload.wikimedia.org/wikipedia/en/f/f2/Hard_To_Kill.jpg",
                    "https://www.youtube.com/watch?v=vwb8S2NTnD0",
                    "https://www.imdb.com/title/tt0099739/?ref_=nv_sr_1")

rescue_dawn = media.Movie("Rescue Dawn",
                    "https://upload.wikimedia.org/wikipedia/en/6/6d/Rescue_Dawn_poster.jpg",
                    "https://www.youtube.com/watch?v=UNm9Tzo5rvI",
                    "https://www.imdb.com/title/tt0462504/?ref_=nv_sr_2")

dark_knight = media.Movie("The Dark Knight",
                    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                    "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                    "https://www.imdb.com/title/tt0468569/?ref_=nv_sr_2")

# Pass each Class Instance into an Array
movies = [seven, fight_club, last_samurai,hard_to_kill,rescue_dawn,dark_knight]

# Pass the movies array to Fresh Tomatoes to serve as HTML
fresh_tomatoes.open_movies_page(movies)
