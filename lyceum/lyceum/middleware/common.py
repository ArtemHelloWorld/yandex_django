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

    def __call__(self, request):
        self.count = (self.count + 1) % 10

        response = self.get_response(request)

        if conf.settings.REVERSE_RU:
            if self.count == 0:
                response.content = flip_ru_words(
                    response.content.decode("utf-8")
                )

        return response
