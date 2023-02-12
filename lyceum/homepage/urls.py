from django.http import HttpResponse
from django.urls import path

from .views import home


def error418(request):
    return HttpResponse("<body>Я чайник.</body>", status=418)


urlpatterns = [
    path("", home, name="homepage"),
    path("coffee/", error418, name="coffee"),
]
