import json 

def read_json_file(file_name):
    with open(file_name,'r') as jsonfile:
        imdb_movie_data = json.load(jsonfile)
    return imdb_movie_data

def get_top_ten_movies_by_imdb_score(file_name):
    imdb_movie_data = read_json_file(file_name)
    movies = [] #{}
    for j in imdb_movie_data:
        movie = j['name'],j['imdb_score']
        movies.append(movie)
    sorted_movies = sorted(movies,key = lambda x: x[1],reverse=True)
    top_ten_movies = sorted_movies[:10]
    return top_ten_movies

res = get_top_ten_movies_by_imdb_score('IMDB Assignment/imdb_movies.json')
for top_movies in res:
    print(f"The movie is \"{top_movies[0]}\",and its imdb score is \"{top_movies[1]}\"")

# def get_top_ten_movies_by_imdb_score(file_name):
#     imdb_movie_data = read_json_file(file_name)
#     # write your logic here to solve the query
#     sorted_movies = sorted(imdb_movie_data, key=lambda x: x['imdb_score'], reverse=True)
#     top_10_movies = sorted_movies[:10]
#     return top_10_movies
# top_movies =  get_top_ten_movies_by_imdb_score('IMDB Assignment/imdb_movies.json')
# for movie in top_movies:
#     print(f"Movie: {movie['name']} with IMDb score: {movie['imdb_score']}")