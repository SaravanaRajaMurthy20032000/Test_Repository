import json

def read_json_file(file_name):
    with open(file_name) as json_file:
        imdb_movie_data = json.load(json_file)
    return imdb_movie_data

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
top_watched  = max(top_genere_watched.items(),key=lambda x: x[1])
print(f"The popular genere watched by audiance  is {list(top_watched)}")