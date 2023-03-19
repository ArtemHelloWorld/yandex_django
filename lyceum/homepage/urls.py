import django.urls

from . import views

app_name = "homepage"

urlpatterns = [
    django.urls.path("", views.home, name="homepage"),
    django.urls.path("coffee/", views.error418, name="coffee"),
]
