django-tmdb
===========

A small TMDB (themoviedatabase) wrapper for Django


## Installation
	1. Put the tmdb.py file in your app folder

	2. Set TMDB_API_KEY and TMDB_BASE_URL in your settings.py
		TMDB_API_KEY = 'yourtmdbapikey'
		TMDB_BASE_URL = 'https://api.themoviedb.org/3/'
	
	3. Import the wrapper in your views.py (or somewhere else)
		from app.tmdb import *
	
	4. Create the instance
		tmdb = TMDB()
	
	5. Use the wrapper functions
		movie_info = tmdb.getMovieInfo(tmdb_id, 'en')