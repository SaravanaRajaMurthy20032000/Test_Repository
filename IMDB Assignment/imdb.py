# importing json module
import json

def read_json_file(file_name):
    with open(file_name) as json_file:
        imdb_movie_data = json.load(json_file)
    return imdb_movie_data

# 1
def top_dir_with_max_movies(file_name):
    imdb_movie_data = read_json_file(file_name)
    dir = {}
    for i in imdb_movie_data:
        director = i['director']
        # print(director)
        if director in dir:
            dir[director] += 1
        else:
            dir[director] = 1
    return dir

top_dir = top_dir_with_max_movies('IMDB Assignment/imdb_movies.json')
top_director = max(top_dir.items(),key=lambda x: x[1])


# 2
def popular_genere_watched_by_most(file_name):
    imdb_movie_data = read_json_file(file_name)
    d = {}
    for i in imdb_movie_data:
        genere = i["genre"]
        if tuple(genere) in d:
            d[tuple(genere)] += 1
        else:
            d[tuple(genere)] = 1
    return d            
top_genere_watched = popular_genere_watched_by_most('IMDB Assignment/imdb_movies.json')


# 3
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


# 4
def least_watched_movies_by_imdb_score(file_name):
    imdb_movie_data = read_json_file(file_name)
    movies = {}
    for j in imdb_movie_data:
        movie = j["name"]
        movies[movie] = j["imdb_score"]
    sorted_movies = sorted(movies.items(),key = lambda x: x[1],reverse=True)[-1:]
    return sorted_movies
result = least_watched_movies_by_imdb_score('IMDB Assignment/imdb_movies.json')


# 5
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

# 
read_json_file('IMDB Assignment/imdb_movies.json')
# 
print(f"The top director is {top_director[0]} and his movies are {top_director[1]}")
print("------------------------------------------")
top_watched  = max(top_genere_watched.items(),key=lambda x: x[1])
print(f"The popular genere watched by audiance  is {list(top_watched)}")
print("------------------------------------------")
for top_movies in res:
    print(f"The movie is \"{top_movies[0]}\",and its imdb score is \"{top_movies[1]}\"")
print("------------------------------------------")
print(f"The least watched movie is \"{result[0][0]}\" and its imdb score is \"{result[0][1]}\"")
print("------------------------------------------")
print(f"the best director in first hundred movies is : {best_director_hundred_movies}")
print("------------------------------------------")
