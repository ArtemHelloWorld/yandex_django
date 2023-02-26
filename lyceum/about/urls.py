import django.urls

from . import views

app_name = "about"

urlpatterns = [
    django.urls.path("", views.description, name="description"),
]
