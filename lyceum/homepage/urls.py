import django.urls

from . import views

app_name = "homepage"

urlpatterns = [
    django.urls.path("", views.HomeView.as_view(), name="homepage"),
    django.urls.path("coffee/", views.Error418.as_view(), name="coffee"),
]
