'''
This project will take you through the process of mashing up data from two different APIs to make movie recommendations.
The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items.
The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).
'''


import requests
import json

#------------------------------------------------------------------------------------------------------------------
## API for tastedive - 377769-Practise-97EF0EAR                                                                    |
## API for OMBD - c4fc0e4f                                                                                         |
#------------------------------------------------------------------------------------------------------------------

def get_movies_from_tastedive(s):
    d={'q':s,'type':'movies','limit':20,'k':'377769-Practise-97EF0EAR'}
    page=requests.get('https://tastedive.com/api/similar',params=d)
    return page.json()

def extract_movie_titles(d):
    x=[a['Name'] for a in d['Similar']['Results'] ]
    return x

def get_related_titles(l):
    lst=[]
    for x in l:
        s=extract_movie_titles(get_movies_from_tastedive(x))
        for a in s:
            if a not in lst:
                lst.append(a)
    return lst

def get_movie_data(movie):
    d={'t':movie,'r':'json','apikey':'c4fc0e4f'}
    page=requests.get('http://www.omdbapi.com/',params=d)
    return (page.json())

def get_movie_rating_RT(d):
    try:
        l=d['Ratings']
        for x in l:
            if x['Source'] == "Rotten Tomatoes" :
                a = x["Value"]
                n=a.index('%')
                return int(a[:n])
            else:
                a = "Not rated"
        return a
    except:
        return "Not rated"

def get_movie_rating_IMDB(d):
    try:
        l=d['imdbRating']
        return l
    except:
        return "Not rated"

movie_name = input("Enter movie name:\t")
x = extract_movie_titles(get_movies_from_tastedive(movie_name))
print("Similar movies: ")
k = 1.0
for i in x:
    print("\t\t",k,' ',i,end=':\n')
    d = get_movie_data(i)
    n = get_movie_rating_RT(d)
    print("\t\t\t\t Rotten Tomatoes Rating:  ",n,)
    n1 = get_movie_rating_IMDB(d)
    print("\t\t\t\t IMDB:  ",n1)
    print("\n")
    k+=1
