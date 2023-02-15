from django import conf


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


class ReverseMiddleware:
    count = 0

    def __init__(self, get_response):
        self.get_response = get_response

    @classmethod
    def checkreverse(cls):
        cls.count = (cls.count + 1) % 10 
        if conf.settings.REVERSE_RU:
            if cls.count == 0:
                return True
        return False

    def __call__(self, request):
        response = self.get_response(request)

        if self.checkreverse():
            response.content = flip_ru_words(
                response.content.decode("utf-8")
            )

        return response
