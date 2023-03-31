import django.conf
import django.core.cache
import django.http


class ReverseMiddleware:
    count = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if self.check_reverse():
            response.content = self.flip_ru_words(
                response.content.decode("utf-8")
            )

        return response

    @classmethod
    def check_reverse(cls):
        cls.count = (cls.count + 1) % 10
        if django.conf.settings.REVERSE_RU:
            if cls.count == 0:
                return True
        return False

    @staticmethod
    def flip_ru_words(input_string):
        result = ""
        substring = ""

        for char in input_string:
            if 1040 <= ord(char) <= 1103:
                substring += char
            else:
                result += substring[::-1]
                result += char
                substring = ""

        return result


class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        key = f'ratelimit:{request.META.get("REMOTE_ADDR")}'
        count = django.core.cache.cache.get(key, 1)
        if not django.conf.settings.RATE_LIMIT_MIDDLEWARE:
            return self.get_response(request)

        if count >= django.conf.settings.REQUESTS_PER_SECOND:
            return django.http.HttpResponse("Too many requests", status=429)
        else:
            django.core.cache.cache.set(key, count + 1, 1)
            return self.get_response(request)
