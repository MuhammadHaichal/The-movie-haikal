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
judul = "Film Dunia"


def indexMovie(request):
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

    # drama movie
    drama_movie = discover.discover_tv_shows(
        {"with_genres": 18, "sort_by": "vote_average.desc", "vote_count.gte": 10}
    )

    if request.method == "POST":
        form = SearchMovie(request.POST)
        # mengecek apakah data di api atau database ada atau tidak
        if form.is_valid():
            data = movie.search(form.cleaned_data["title"])
            context = {"response_data": data, "form": form, "title": judul}
            return render(request, "film/listResultSearch.html", {"context": context})

    else:
        form = SearchMovie()

    context = {
        "movie_kids": movie_kids,
        "popular_movie": popular_movie,
        "drama_movie": drama_movie,
        "form": form,
        "title": judul,
    }

    return render(request, "film/index.html", {"context": context})


def detailsMovie(request, pk):
    detail = movie.details(pk)  ## detail for movie on id movie

    if request.method == "POST":
        form = SearchMovie(request.POST)

        # mengecek apakah data di api atau database ada atau tidak
        if form.is_valid():
            data = movie.search(form.cleaned_data["title"])
            context = {"response_data": data, "form": form}
            return render(request, "film/listResultSearch.html", {"context": context})

    else:
        form = SearchMovie()

    context = {"title": judul, "data_detail": detail, "form": form}
    return render(request, "film/detailFilm.html", {"context": context})
