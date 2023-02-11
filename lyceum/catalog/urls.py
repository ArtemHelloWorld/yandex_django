from django.urls import path

from .views import item_list, item_detail

urlpatterns = [
    path("", item_list, name="item_list"),
    path("<int:item_pk>/", item_detail, name="item_detail"),
]
