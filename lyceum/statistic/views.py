import django.contrib.auth.mixins
import django.contrib.auth.models
import django.db.models
import django.http
import django.shortcuts
import django.views.generic

import catalog.models
import rating.models


class IndexView(django.views.generic.TemplateView):
    template_name = "statistic/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = django.contrib.auth.models.User.objects.filter(
            is_active=True
        ).only("username")
        return context


class UserStatisticView(django.views.generic.TemplateView):
    template_name = "statistic/user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = django.contrib.auth.models.User.objects.only(
            "username", "email"
        ).get(id=kwargs.get("user_pk"))

        reviews_count = user.reviews.count()
        avg_rating = user.reviews.aggregate(
            avg_rating=django.db.models.Avg("rating")
        )["avg_rating"]

        context["worst_item"] = (
            user.reviews.order_by("rating", "-created_at").first().item
            if reviews_count > 0
            else None
        )
        context["best_item"] = (
            user.reviews.order_by("-rating", "-created_at").first().item
            if reviews_count > 0
            else None
        )
        context["reviews_count"] = reviews_count
        context["avg_rating"] = avg_rating
        context["user"] = user
        
        return context


class ItemStatisticView(django.views.generic.TemplateView):
    template_name = "statistic/item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        item = catalog.models.Item.objects.published().get(
            id=kwargs.get("item_pk")
        )
        reviews_count = item.reviews.count()

        last_minimum_rating = item.reviews.order_by("rating", "-created_at").first() if reviews_count > 0 else None

        last_maximum_rating = item.reviews.order_by("-rating", "-created_at").first() if reviews_count > 0 else None

        context["item"] = item
        context["reviews_count"] = reviews_count
        context["last_minimum_rating"] = last_minimum_rating
        context["last_maximum_rating"] = last_maximum_rating
        
        return context


class UserReviewsListView(
    django.contrib.auth.mixins.LoginRequiredMixin, django.views.generic.ListView
):
    template_name = "statistic/user_reviews.html"
    context_object_name = "reviews"

    def get_queryset(self):
        return (
            rating.models.Review.objects.filter(user=self.request.user)
            .select_related("item")
            .only("rating", "item__name")
            .order_by("-rating")
        )
