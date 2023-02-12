from django.http import HttpResponse


def flip_russian_subsequences(input_string):
    result = ""
    substring = ""

    for char in input_string:
        if 1040 <= ord(char) <= 1103:
            substring += char
        else:
            result += substring[::-1]
            substring = ''
            result += char

    return result


class ReverseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.counter = 0

    def __call__(self, request):
        self.counter += 1

        response = self.get_response(request)

        if self.counter % 10 == 0:
            response.content = flip_russian_subsequences(response.content.decode("utf-8"))

        return response
