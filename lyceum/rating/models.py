import django.contrib.auth.models
import django.core.validators
import django.db.models

import catalog.models


class ReviewManager(django.db.models.Manager):
    def get(self, **kwargs):
        queryset = self.get_queryset().filter(**kwargs)
        if queryset:
            return queryset[0]
        return None


class Review(django.db.models.Model):
    class Rating(django.db.models.IntegerChoices):
        VERY_BAD = (1, "1")
        BAD = (2, "2")
        NEUTRAL = (3, "3")
        GOOD = (4, "4")
        VERY_GOOD = (5, "5")

    objects = ReviewManager()

    rating = django.db.models.PositiveSmallIntegerField(
        choices=Rating.choices,
        verbose_name="оценка",
        default=Rating.VERY_GOOD,
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
    created_at = django.db.models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания"
    )

    class Meta:
        verbose_name = "отзыв/оценка товара"
        verbose_name_plural = "отзыв/оценка товара"
