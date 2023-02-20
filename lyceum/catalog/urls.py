import catalog.converters
import catalog.views

import django.urls


django.urls.register_converter(
    catalog.converters.CustomPositiveIntegerConverter, "customint"
)

urlpatterns = [
    django.urls.path("", catalog.views.item_list, name="item_list"),
    django.urls.path(
        "<int:item_pk>/", catalog.views.item_detail, name="item_detail"
    ),
    django.urls.re_path(
        r"^re/(?P<reint>[1-9][0-9]*)/",
        catalog.views.item_detail_re,
        name="item_detail_re",
    ),
    django.urls.path(
        "converter/<customint:custom_int>/",
        catalog.views.custom_converter,
        name="custom_converter",
    ),
]
