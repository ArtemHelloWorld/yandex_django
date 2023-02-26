import django.conf


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
