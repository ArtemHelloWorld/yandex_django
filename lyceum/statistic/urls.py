import django.urls

import core.converters
import statistic.views

app_name = "statistic"

django.urls.register_converter(
    core.converters.CustomPositiveIntegerConverter, "customint"
)


urlpatterns = [
    django.urls.path(
        "",
        statistic.views.IndexView.as_view(),
        name="index",
    ),
    django.urls.path(
        "user/<customint:user_pk>",
        statistic.views.UserStatisticView.as_view(),
        name="user",
    ),
    django.urls.path(
        "item/<customint:item_pk>",
        statistic.views.ItemStatisticView.as_view(),
        name="item",
    ),
    django.urls.path(
        "reviews",
        statistic.views.UserReviewsListView.as_view(),
        name="user_reviews",
    ),
]
