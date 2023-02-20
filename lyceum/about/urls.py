import django.urls

from . import views

urlpatterns = [
    django.urls.path("", views.description, name="description"),
]
