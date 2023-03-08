import datetime
import random

import catalog.models
import django.db.models


class ItemManager(django.db.models.Manager):
    def published(self, is_on_main=False, ordering="name"):
        return (
            self.get_queryset()
            .select_related("category")
            .select_related("image")
            .prefetch_related(
                django.db.models.Prefetch(
                    "tags",
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True
                    ).only("name"),
                )
            )
            .only(
                "name",
                "text",
                "image__image_main",
                "category__name",
            )
            .filter(
                is_published=True,
                is_on_main__in=(True,) if is_on_main else (True, False),
            )
            .order_by(ordering, "id")
        )

    def this_week(self, number_of_items):
        time_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
        items_ids = (
            self.get_queryset()
            .filter(
                is_published=True,
                date_created__gte=time_week_ago,
            )
            .values_list("id", flat=True)
        )

        if len(items_ids) > number_of_items:
            random_numbers = random.sample(list(items_ids), number_of_items)
        else:
            random_numbers = items_ids

        return (
            self.get_queryset()
            .select_related("category")
            .select_related("image")
            .prefetch_related(
                django.db.models.Prefetch(
                    "tags",
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True
                    ).only("name"),
                )
            )
            .only(
                "name",
                "text",
                "image__image_main",
                "category__name",
            )
            .filter(id__in=random_numbers)
            .order_by("-id")
        )

    def friday(self, number_of_items):
        return (
            self.get_queryset()
            .select_related("category")
            .select_related("image")
            .prefetch_related(
                django.db.models.Prefetch(
                    "tags",
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True
                    ).only("name"),
                )
            )
            .only(
                "name",
                "text",
                "image__image_main",
                "category__name",
            )
            .filter(is_published=True, date_updated__week_day=6)
            .order_by("-id")[:number_of_items]
        )

    def unverified(self):
        return (
            self.get_queryset()
            .select_related("category")
            .select_related("image")
            .prefetch_related(
                django.db.models.Prefetch(
                    "tags",
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True
                    ).only("name"),
                )
            )
            .only(
                "name",
                "text",
                "image__image_main",
                "category__name",
            )
            .filter(
                is_published=True,
                date_created=django.db.models.F("date_updated"),
            )
        )
