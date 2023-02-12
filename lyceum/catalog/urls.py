from django.urls import path, re_path, register_converter

from . import views, converters

register_converter(converters.CustomPositiveIntegerConverter, 'customint')

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("<int:item_pk>/", views.item_detail, name="item_detail"),

    re_path(r"^re/(?P<reint>[0-9]+)/", views.item_detail_re, name="item_detail_re"),
    path("converter/<customint:custom_int>/", views.custom_converter, name="custom_converter"),
]
