import django.urls

import catalog.converters
import catalog.views

app_name = "catalog"

django.urls.register_converter(
    catalog.converters.CustomPositiveIntegerConverter, "customint"
)


urlpatterns = [
    django.urls.path(
        "", catalog.views.ItemListView.as_view(), name="item_list"
    ),
    django.urls.path(
        "<customint:item_pk>/",
        catalog.views.ItemDetailView.as_view(),
        name="item_detail",
    ),
    django.urls.path(
        "downloadimagemain/<customint:image_pk>/",
        catalog.views.DownloadImageMainView.as_view(),
        name="download_image_main",
    ),
    django.urls.path(
        "downloadimagegallery/<customint:image_pk>/",
        catalog.views.DownloadImageGalleryView.as_view(),
        name="download_image_gallery",
    ),
    django.urls.path(
        "new", catalog.views.ItemsNewView.as_view(), name="items_new"
    ),
    django.urls.path(
        "friday", catalog.views.ItemsFridayView.as_view(), name="items_friday"
    ),
    django.urls.path(
        "unverified",
        catalog.views.ItemsUnverifiedView.as_view(),
        name="items_unverified",
    ),
]
