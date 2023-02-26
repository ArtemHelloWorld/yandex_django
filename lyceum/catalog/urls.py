import catalog.converters
import catalog.views

import django.urls


app_name = "catalog"

django.urls.register_converter(
    catalog.converters.CustomPositiveIntegerConverter, "customint"
)


urlpatterns = [
    django.urls.path("", catalog.views.item_list, name="item_list"),
    django.urls.path(
        "<customint:item_pk>/", catalog.views.item_detail, name="item_detail"
    ),
]
