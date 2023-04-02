import django.urls

import core.converters
import rating.views

app_name = "rating"

django.urls.register_converter(
    core.converters.CustomPositiveIntegerConverter, "customint"
)


urlpatterns = [
    django.urls.path(
        "delete/<customint:item_pk>",
        rating.views.DeleteView.as_view(),
        name="delete",
    ),
]
