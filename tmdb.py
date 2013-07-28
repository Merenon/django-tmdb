from settings import TMDB_API_KEY, TMDB_BASE_URL
from django.core.cache import cache
import requests
from operator import itemgetter
import urllib as ul
import hashlib

class TMDB(object):

	def __init__(self):
		
		if TMDB_API_KEY is '':
			raise Exception('No TMDB_API_KEY given')
		
		if TMDB_BASE_URL is '':
			raise Exception('No TMDB_BASE_URL given')
		
		self.api_key = TMDB_API_KEY
		self.base_url = TMDB_BASE_URL
		self.cache_time = 60*60*24*30 # cache for 30 days

	def getMovieInfo(self, movie_id, lang='en'):
		movie_info = None
		movie_info = cache.get('tmdb_movie_info_%s_%s' % (lang, movie_id))

		if movie_info is None:
			tmdb_request = requests.get('%smovie/%s?api_key=%s&language=%s' % (self.base_url, movie_id, self.api_key, lang))
			
			if tmdb_request.status_code == 200:
				movie_info = tmdb_request.json()
				cache.set('tmdb_movie_info_%s_%s' % (lang, movie_id), movie_info, self.cache_time)
		
		return movie_info

	def getMovieCast(self, movie_id, lang='en'):
		movie_cast = None
		movie_cast = cache.get('tmdb_movie_cast_%s_%s' % (lang, movie_id))

		if movie_cast is None:
			tmdb_request = requests.get('%smovie/%s/casts?api_key=%s&language=%s' % (self.base_url, movie_id, self.api_key, lang))
			
			if tmdb_request.status_code == 200:
				movie_cast = tmdb_request.json()
				cache.set('tmdb_movie_cast_%s_%s' % (lang, movie_id), movie_cast, self.cache_time)
		
		return movie_cast['cast']

	def searchMovie(self, movie_name, lang='en'):
		movies = None
		name_hash = hashlib.md5(movie_name).hexdigest()

		movies = cache.get('tmdb_search_movie_%s_%s' % (lang, name_hash))

		if movies is None:
			name = movie_name.encode("utf-8").replace("-", " ")
			tmdb_request = requests.get('%ssearch/movie?api_key=%s&language=%s&query=%s' % (self.base_url, self.api_key, lang, name))
		
			if tmdb_request.status_code == 200:
				movies = tmdb_request.json()
				cache.set('tmdb_search_movie_%s_%s' % (lang, name_hash), movies, self.cache_time)
		
		return movies['results']

