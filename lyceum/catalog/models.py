import catalog.model_managers
import catalog.validators
import django.db.models
import django.urls
import django_cleanup.signals
import sorl.thumbnail
import tinymce

import core.models


class Item(core.models.NameFieldMixin, core.models.IsPublishedFieldMixin):
    objects = catalog.model_managers.ItemManager()

    text = tinymce.HTMLField(
        validators=[
            catalog.validators.ValidateMustContain("превосходно", "роскошно")
        ],
        verbose_name="описание",
        help_text="Придумайте описание. Текст должен "
        "включать слова превосходно или роскошно",
    )
    category = django.db.models.ForeignKey(
        "category",
        on_delete=django.db.models.CASCADE,
        verbose_name="категория",
        help_text="Выберите категорию или добавьте новую",
    )
    tags = django.db.models.ManyToManyField(
        "tag",
        verbose_name="теги",
        help_text="Выберите тег или создайте новый",
    )
    image = django.db.models.OneToOneField(
        "ItemImageMain",
        verbose_name="главное фото",
        on_delete=django.db.models.CASCADE,
    )

    is_on_main = django.db.models.BooleanField(
        default=False,
        verbose_name="добавить на главную страницу",
        help_text="Поставьте галочку, если хотите "
        "отобразить товар на главной странице",
    )
    date_created = django.db.models.DateField(
        auto_now_add=True, verbose_name="дата создания"
    )
    date_updated = django.db.models.DateField(
        auto_now=True, verbose_name="дата последнего изменения"
    )

    def get_absolute_url(self):
        return django.urls.reverse(
            "catalog:item_detail", kwargs={"item_pk": self.pk}
        )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class Tag(
    core.models.NameFieldMixin,
    core.models.IsPublishedFieldMixin,
    core.models.SlugFieldMixin,
    core.models.NormalizedNameFieldMixin,
):
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"


class Category(
    core.models.NameFieldMixin,
    core.models.IsPublishedFieldMixin,
    core.models.SlugFieldMixin,
    core.models.NormalizedNameFieldMixin,
):
    weight = django.db.models.PositiveSmallIntegerField(
        default=150,
        verbose_name="масса",
        help_text="Укажите массу",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class ItemImageMain(django.db.models.Model):
    image_main = django.db.models.ImageField(upload_to="item/main/%Y/%m/%d")

    class Meta:
        verbose_name = "фото главное"
        verbose_name_plural = "фото главные"


class ItemImageGallery(django.db.models.Model):
    image_gallery = django.db.models.ImageField(
        upload_to="item/gallery/%Y/%m/%d"
    )
    item = django.db.models.ForeignKey(
        Item,
        on_delete=django.db.models.CASCADE,
        null=True,
        related_name="gallery",
    )

    class Meta:
        verbose_name = "фото галерея"
        verbose_name_plural = "фото галерея"


# clearing cache
def sorl_delete(**kwargs):
    sorl.thumbnail.delete(kwargs["file"])


django_cleanup.signals.cleanup_pre_delete.connect(sorl_delete)
