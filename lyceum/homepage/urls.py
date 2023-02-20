import django.urls

from . import views

urlpatterns = [
    django.urls.path("", views.home, name="homepage"),
    django.urls.path("coffee/", views.error418, name="coffee"),
]
