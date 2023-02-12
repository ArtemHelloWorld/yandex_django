from django.http import HttpResponse
from django.urls import path

from . import views


def error418(request):
    return HttpResponse("<body>Я чайник.</body>", status=418)


urlpatterns = [
    path("", views.home, name="homepage"),
    path("coffee/", error418, name="coffee"),
]
