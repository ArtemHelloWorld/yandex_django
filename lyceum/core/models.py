import re

import django.db
import django.db.models
import django.forms

import transliterate


def normalize_name(value):
    value = value.lower()
    value = re.sub(r"[^\w]", "", value)
    value = transliterate.translit(value, "ru", reversed=True)

    return value


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
        name = getattr(self, "name")
        normalized = normalize_name(name)
        try:
            setattr(self, "name_normalized", normalized)
            super(NormalizedNameFieldMixin, self).save(*args, **kwargs)
        except django.db.IntegrityError:
            raise django.db.IntegrityError(
                "Подобное имя уже существует. "
                "Пожалуста придумайте более уникально имя."
                " Учтите, что пробелы, знаки препинания, "
                "большие буквы не влияют на уникальность имени"
            )

    def unique_error_message(self, model_class, unique_check):
        return "Custom errrrorrr"

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
