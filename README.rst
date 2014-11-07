=====
django-tmdb
=====

A small TMDB (themoviedatabase) API v3 wrapper for Django


Requirements
-----------
1. Python module "requests"

2. TMDB Api Key

3. Enabled caching in Django

Install
-----------

Simply install django-tmdb with pip

    pip install django-tmdb

Quick start
-----------

1. Install "requests" (e.g. with pip install requests)
2. Add "tmdb" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'tmdb',
    )

3. Set TMDB_API_KEY in your settings.py

    TMDB_API_KEY = 'yourtmdbapikey'

4. Import the wrapper where needed (e.g. in your views.py)

    from tmdb import TMDB

5. Create the instance

    tmdb = TMDB()

6. Use the wrapper functions

    movie_info = tmdb.getMovieInfo(tmdb_id, 'en')