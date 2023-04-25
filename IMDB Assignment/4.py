import json 

def read_json_file(file_name):
    with open(file_name,'r') as jsonfile:
        imdb_movie_data = json.load(jsonfile)
    return imdb_movie_data

def least_watched_movies_by_imdb_score(file_name):
    imdb_movie_data = read_json_file(file_name)
    movies = {}
    for j in imdb_movie_data:
        movie = j["name"]
        movies[movie] = j["imdb_score"]
    sorted_movies = sorted(movies.items(),key = lambda x: x[1],reverse=True)[-1:]
    return sorted_movies

result = least_watched_movies_by_imdb_score('IMDB Assignment/imdb_movies.json')
print(f"The least watched movie is \"{result[0][0]}\" and its imdb score is \"{result[0][1]}\" ")

# def least_watched_movie_by_imdb_score(file_name):
#     imdb_movie_data = read_json_file(file_name)
#     # write your logic here to solve the query
#     d ={}
#     for i in imdb_movie_data:
#         movie_name = i["name"]
#         d[movie_name] = i["imdb_score"]
#     return d
# least_watched_movie_imdb_score = least_watched_movie_by_imdb_score('IMDB Assignment/imdb_movies.json')
# least_watched_movie_imdb_score = min(least_watched_movie_imdb_score.items(),key = lambda x:x[1])
# print(f"the least watched movie based on their imdb score is : {least_watched_movie_imdb_score}")