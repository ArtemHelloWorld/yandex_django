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
