import django.http


def home(request):
    return django.http.HttpResponse("<body>Главная</body>")


def error418(request):
    return django.http.HttpResponse("<body>Я чайник.</body>", status=418)
