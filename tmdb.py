from settings import TMDB_API_KEY, TMDB_BASE_URL
from django.core.cache import cache
import requests

class TMDB(object):

	def __init__(self, lang='en'):
		self.lang = lang
		self.api_key = TMDB_API_KEY
		self.base_url = TMDB_BASE_URL
		self.cache_time = 60*60*24*30 # cache for 30 days

	def getMovieInfo(self, id):
		movie_info = cache.get('tmdb_movie_info_%s_%s' % (self.lang, id))

		if movie_info is None:
			tmdb_request = requests.get('%smovie/%s?api_key=%s&language=%s' % (self.base_url, id, self.api_key, self.lang))
			
			if tmdb_request.status_code == 200:
				movie_info = tmdb_request.json()
				cache.set('tmdb_movie_info_%s_%s' % (self.lang, id), movie_info, self.cache_time)
		
		return movie_info
