import django.urls

import catalog.converters
import catalog.views

app_name = "catalog"

django.urls.register_converter(
    catalog.converters.CustomPositiveIntegerConverter, "customint"
)


urlpatterns = [
    django.urls.path("", catalog.views.item_list, name="item_list"),
    django.urls.path(
        "<customint:item_pk>/",
        catalog.views.item_detail,
        name="item_detail",
    ),
    django.urls.path(
        "downloadimagemain/<customint:image_pk>/",
        catalog.views.download_image_main,
        name="download_image_main",
    ),
    django.urls.path(
        "downloadimagegallery/<customint:image_pk>/",
        catalog.views.download_image_gallery,
        name="download_image_gallery",
    ),
    django.urls.path("new", catalog.views.items_new, name="items_new"),
    django.urls.path(
        "friday", catalog.views.items_friday, name="items_friday"
    ),
    django.urls.path(
        "unverified", catalog.views.items_unverified, name="items_unverified"
    ),
]
