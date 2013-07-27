django-tmdb
===========

A small TMDB (themoviedatabase) wrapper for Django


## Installation
	1. Set *TMDB_API_KEY* and *TMDB_BASE_URL* in your settings.py
		`TMDB_API_KEY = 'yourtmdbapikey'`
		`TMDB_BASE_URL = 'https://api.themoviedb.org/3/'`
	2. Import the wrapper in your views.py (or somewhere else)
		`from app.tmdb import *`
	3. Create the instance and set the language as parameter
		`tmdb = TMDB('en')`
	4. Use the wrapper functions
		`movie_info = tmdb.getMovieInfo(tmdb_id)`