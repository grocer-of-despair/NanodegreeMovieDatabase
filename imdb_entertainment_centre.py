import imdb
import fresh_tomatoes


ia = imdb.IMDb()

s_result = ia.search_movie("Seven")

#for item in s_result:
#    print item['long imdb canonical title'], item.movieID

seven = s_result[0]
ia.update(seven)
director = seven['director']
plot = seven['plot']
actors = seven['cast']
videoclips = seven['video clips']
cover = seven['cover']
print(videoclips[0])
print(cover[0])


movies = [seven]
fresh_tomatoes.open_movies_page(movies)
