# middlewares.py

from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.conf import settings

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Use the client's IP address as the key for rate limiting
        ip_address = request.META.get('REMOTE_ADDR')
        cache_key = f'ratelimit:{ip_address}'
        request_count = cache.get(cache_key, 0)
        
        rate_limit = settings.RATE_LIMIT
        time_window = settings.TIME_WINDOW

        if request_count >= rate_limit:
            return HttpResponseForbidden("Rate limit exceeded")

        cache.set(cache_key, request_count + 1, timeout=time_window)

        response = self.get_response(request)
        return response
