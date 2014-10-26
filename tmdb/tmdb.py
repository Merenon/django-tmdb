import hashlib
import requests
from django.conf import settings
from django.core.cache import cache


class TMDB(object):

    def __init__(self):

        if settings.TMDB_API_KEY is '':
            raise Exception('No TMDB_API_KEY given')

        if settings.TMDB_BASE_URL is '':
            raise Exception('No TMDB_BASE_URL given')

        self.api_key = settings.TMDB_API_KEY
        self.base_url = settings.TMDB_BASE_URL
        self.cache_time = 60 * 60 * 24 * 30  # cache for 30 days

    def getMovieInfo(self, id, lang='en'):
        movie_info = None
        movie_info = cache.get('tmdb_movie_info_%s_%s' % (lang, id))

        if movie_info is None:
            tmdb_request = requests.get('%smovie/%s?api_key=%s&language=%s' % (self.base_url, id, self.api_key, lang))

            if tmdb_request.status_code == 200:
                movie_info = tmdb_request.json()
                cache.set('tmdb_movie_info_%s_%s' % (lang, id), movie_info, self.cache_time)

        return movie_info

    def getMovieCast(self, id, lang='en'):
        movie_cast = None
        movie_cast = cache.get('tmdb_movie_cast_%s_%s' % (lang, id))

        if movie_cast is None:
            tmdb_request = requests.get('%smovie/%s/casts?api_key=%s&language=%s' % (self.base_url, id, self.api_key, lang))

            if tmdb_request.status_code == 200:
                movie_cast = tmdb_request.json()
                cache.set('tmdb_movie_cast_%s_%s' % (lang, id), movie_cast, self.cache_time)

        return movie_cast['cast']

    def getMovieImages(self, id, lang='en'):
        movie_images = None
        movie_images = cache.get('tmdb_movie_images_%s_%s' % (lang, id))

        if movie_images is None:
            tmdb_request = requests.get('%smovie/%s/images?api_key=%s&language=%s' % (self.base_url, id, self.api_key, lang))

            if tmdb_request.status_code == 200:
                movie_images = tmdb_request.json()
                cache.set('tmdb_movie_images_%s_%s' % (lang, id), movie_images, self.cache_time)

        return movie_images

    def getTVInfo(self, id, lang='en'):
        tv_info = None
        tv_info = cache.get('tmdb_tv_info_%s_%s' % (lang, id))

        if tv_info is None:
            tmdb_request = requests.get('%stv/%s?api_key=%s&language=%s' % (self.base_url, id, self.api_key, lang))

            if tmdb_request.status_code == 200:
                tv_info = tmdb_request.json()
                cache.set('tmdb_tv_info_%s_%s' % (lang, id), tv_info, self.cache_time)

        return tv_info

    def getTVImages(self, id, lang='en'):
        tv_images = None
        tv_images = cache.get('tmdb_tv_images_%s_%s' % (lang, id))

        if tv_images is None:
            tmdb_request = requests.get('%stv/%s/images?api_key=%s&language=%s' % (self.base_url, id, self.api_key, lang))

            if tmdb_request.status_code == 200:
                tv_images = tmdb_request.json()
                cache.set('tmdb_tv_images_%s_%s' % (lang, id), tv_images, self.cache_time)

        return tv_images

    def getTVSeason(self, id, season, lang='en'):
        tv_season = None
        tv_season = cache.get('tmdb_tv_season_%s_%s' % (lang, id))

        if tv_season is None:
            tmdb_request = requests.get('%stv/%s/season/%s?api_key=%s&language=%s' % (self.base_url, id, season, self.api_key, lang))

            if tmdb_request.status_code == 200:
                tv_season = tmdb_request.json()
                cache.set('tmdb_tv_season_%s_%s' % (lang, id), tv_season, self.cache_time)

        return tv_season

    def searchMovie(self, name, lang='en'):
        results = None
        name_hash = hashlib.md5(name).hexdigest()

        results = cache.get('tmdb_search_movie_%s_%s' % (lang, name_hash))

        if results is None:
            tmdb_request = requests.get('%ssearch/movie?api_key=%s&language=%s&query=%s' % (self.base_url, self.api_key, lang, name.encode("utf-8")))

            if tmdb_request.status_code == 200:
                results = tmdb_request.json()
                cache.set('tmdb_search_movie_%s_%s' % (lang, name_hash), results, self.cache_time)

        return results['results']

    def searchMulti(self, name, lang='en'):
        results = None
        name_hash = hashlib.md5(name).hexdigest()

        results = cache.get('tmdb_search_multi_%s_%s' % (lang, name_hash))

        if results is None:
            tmdb_request = requests.get('%ssearch/multi?api_key=%s&language=%s&query=%s' % (self.base_url, self.api_key, lang, name.encode("utf-8")))

            if tmdb_request.status_code == 200:
                results = tmdb_request.json()
                cache.set('tmdb_search_multi_%s_%s' % (lang, name_hash), results, self.cache_time)

        return results['results']

    def searchTV(self, name, lang='en'):
        results = None
        name_hash = hashlib.md5(name).hexdigest()

        results = cache.get('tmdb_search_tv_%s_%s' % (lang, name_hash))

        if results is None:
            tmdb_request = requests.get('%ssearch/tv?api_key=%s&language=%s&query=%s' % (self.base_url, self.api_key, lang, name.encode("utf-8")))

            if tmdb_request.status_code == 200:
                results = tmdb_request.json()
                cache.set('tmdb_search_tv_%s_%s' % (lang, name_hash), results, self.cache_time)

        return results['results']
