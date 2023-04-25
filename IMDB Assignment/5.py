#  5. Print the best director in the first hundred movies.
import json

def read_json_file(file_name):
    with open(file_name,'r') as jsonfile:
        imdb_movie_data = json.load(jsonfile)
    return imdb_movie_data

def get_best_director_in_first_hundred_movies(file_name):
    imdb_movie_data = read_json_file(file_name)
    best_director = {}
    for movie in imdb_movie_data:
        director = movie["director"]
        best_director[director] = movie["imdb_score"]
    return best_director
best_director_in_hundred_movies = get_best_director_in_first_hundred_movies('IMDB Assignment/imdb_movies.json')
best_director_in_hundred_movies = sorted(best_director_in_hundred_movies, key=lambda x: x[1],reverse=True)[:100]
best_director_hundred_movies = max(best_director_in_hundred_movies, key=lambda x: x[1])
print(f"the best director in first hundred movies is : {best_director_hundred_movies}")