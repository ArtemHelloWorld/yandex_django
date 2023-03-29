import django.contrib.auth.models
import django.core.validators
import django.db.models

import catalog.models


class ReviewManager(django.db.models.Manager):
    def get_rating(self, **kwargs):
        queryset = self.get_queryset().filter(**kwargs)
        if queryset:
            return queryset[0].rating
        return None


class Review(django.db.models.Model):
    class Rating(django.db.models.IntegerChoices):
        VERY_BAD = (1, "Very bad")
        BAD = (2, "Bad")
        NEUTRAL = (3, "Neutral")
        GOOD = (4, "Good")
        VERY_GOOD = (5, "Very good")

    objects = ReviewManager()

    rating = django.db.models.SmallIntegerField(
        choices=Rating.choices,
        verbose_name="оценка",
        help_text="Целое число от 1 до 5",
    )
    item = django.db.models.ForeignKey(
        catalog.models.Item,
        on_delete=django.db.models.CASCADE,
        related_name="reviews",
        verbose_name="товар",
    )
    user = django.db.models.ForeignKey(
        django.contrib.auth.models.User,
        on_delete=django.db.models.CASCADE,
        related_name="reviews",
        verbose_name="пользователь",
    )

    class Meta:
        verbose_name = "отзыв/оценка товара"
        verbose_name_plural = "отзыв/оценка товара"
