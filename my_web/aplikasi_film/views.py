from django.shortcuts import render
import os


# modul diperlukan
from dotenv import load_dotenv
from tmdbv3api import TMDb, Movie, Discover
from .forms import SearchMovie

# inilisasi file env
load_dotenv()
API_KEY = os.getenv("api_key")

# inilisasi for tmdb
tmdb = TMDb()
movie = Movie()
discover = Discover()
tmdb.api_key = API_KEY


def index(request):
    # most popular popular kids movies
    movie_kids = discover.discover_movies(
        {
            "certification_country": "US",
            "certification.lte": "G",
            "sort_by": "popularity.desc",
        }
    )

    # most popular movie
    popular_movie = discover.discover_tv_shows({"sort_by": "popularity.desc"})

    if request.method == "POST":
        form = SearchMovie(request.POST)
        # mengecek apakah data di api atau database ada atau tidak
        if form.is_valid():
            data = movie.search(form.cleaned_data['title'])
            context = {"response_data": data, "form": form}
            return render(request, "film/listResultSearch.html", {"context": context})
    
    else:
        form = SearchMovie()

    context = {
       "movie_kids": movie_kids,
       "popular_movie": popular_movie,
       "form" : form,
    }

    return render(request, "film/index.html", {"context": context})


def detailsMovie(request, pk):
    detail = movie.details(pk)
    context = {
            'data_detail' : detail,
            }
    return render(request, 'film/detailFilm.html', {'context' : context})
