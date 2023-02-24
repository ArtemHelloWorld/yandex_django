import re

import django.db
import django.db.models
import django.forms

import transliterate


class NameFieldMixin(django.db.models.Model):
    name = django.db.models.CharField(
        max_length=150,
        verbose_name="название",
        help_text="Укажите название. Максимум 150 символов",
    )

    class Meta:
        abstract = True


class NormalizedNameFieldMixin(django.db.models.Model):
    name_normalized = django.db.models.CharField(
        max_length=200,
        unique=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        self.name_normalized = self._generate_normalize_name()
        super().save(*args, **kwargs)

    def _generate_normalize_name(self):
        normalized = self.name.lower()
        normalized = re.sub(r"\W", "", normalized)
        normalized = transliterate.translit(normalized, "ru", reversed=True)

        if self.__class__.objects.filter(name_normalized=normalized).exists():
            raise django.db.IntegrityError(
                "Подобное имя уже существует. "
                "Пожалуста придумайте более уникально имя. "
                "Учтите, что пробелы, знаки препинания, "
                "большие буквы не влияют на уникальность имени"
            )

        return normalized

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
