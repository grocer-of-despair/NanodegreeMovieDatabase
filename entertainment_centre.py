import media
import fresh_tomatoes

# INSTANCE of a Class
seven = media.Movie("Seven",
                        "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives",
                        "https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg",
                        "https://www.youtube.com/watch?v=znmZoVkCjpI")

# INSTANCE of a Class
fight_club = media.Movie("Fight Club",
                    "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more",
                    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                    "https://www.youtube.com/watch?v=SUXWAEX2jlg")

# INSTANCE of a Class
last_samurai = media.Movie("The Last Samurai",
                    "An American military advisor embraces the Samurai culture he was hired to destroy after he is captured in battle",
                    "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Last_Samurai.jpg",
                    "https://www.youtube.com/watch?v=T50_qHEOahQ")

# INSTANCE of a Class
hard_to_kill = media.Movie("Hard To Kill",
                    "Left for dead with his wife killed in their house, L.A. Detective Mason Storm will have to make a quick recovery, expose those behind the murder and take revenge",
                    "https://upload.wikimedia.org/wikipedia/en/f/f2/Hard_To_Kill.jpg",
                    "https://www.youtube.com/watch?v=vwb8S2NTnD0")

# INSTANCE of a Class
rescue_dawn = media.Movie("The Last Samurai",
                    "A U.S. fighter pilot's epic struggle of survival after being shot down on a mission over Laos during the Vietnam War.",
                    "https://upload.wikimedia.org/wikipedia/en/6/6d/Rescue_Dawn_poster.jpg",
                    "https://www.youtube.com/watch?v=UNm9Tzo5rvI")

# INSTANCE of a Class
dark_knight = media.Movie("The Dark Knight",
                    "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [seven, fight_club, last_samurai,hard_to_kill,rescue_dawn,dark_knight]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__name__)
