import django.db.models


class NameFieldMixin(django.db.models.Model):
    name = django.db.models.CharField(
        max_length=150,
        verbose_name="название",
        help_text="Укажите название. Максимум 150 символов",
    )

    class Meta:
        abstract = True


class IsPublishedFieldMixin(django.db.models.Model):
    is_published = django.db.models.BooleanField(
        default=True,
        verbose_name="опубликовано",
        help_text="Уберите галочку, если хотите скрыть запись",
    )

    class Meta:
        abstract = True


class SlugFieldMixin(django.db.models.Model):
    slug = django.db.models.SlugField(
        max_length=200,
        verbose_name="слаг",
        help_text="Укажите слаг, который будет отображаться в ссылке",
    )

    class Meta:
        abstract = True
