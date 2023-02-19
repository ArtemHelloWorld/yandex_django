import django.db.models


class AbstractModel(django.db.models.Model):
    name = django.db.models.CharField(
        max_length=150,
        verbose_name="Название",
        help_text="Укажите название. Максимум 150 символов",
    )
    is_published = django.db.models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Уберите галочку, если хотите скрыть запись",
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name[:20]


class AbstractModelWithSlug(AbstractModel):
    slug = django.db.models.SlugField(
        max_length=200,
        verbose_name="Слаг",
        help_text="Укажите слаг, который будет отображаться в ссылке",
    )

    class Meta:
        abstract = True
