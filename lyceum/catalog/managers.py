import datetime

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

    def this_week(self):
        time_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
        return (
            self.get_queryset()
            .filter(
                is_published=True,
                date_created__gte=time_week_ago,
            )
            .values_list("id", flat=True)
        )

    def friday(self):
        return (
            self.get_queryset()
            .filter(is_published=True, date_updated__week_day=6)
            .values_list("id", flat=True)
            .order_by("-date_created")
        )

    def unverified(self):
        return self.get_queryset().filter(
            is_published=True, date_created=django.db.models.F("date_updated")
        )
