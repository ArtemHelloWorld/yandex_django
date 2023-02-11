from django.urls import path

from .views import item_detail, item_list

urlpatterns = [
    path("", item_list, name="item_list"),
    path("<int:item_pk>/", item_detail, name="item_detail"),
]
