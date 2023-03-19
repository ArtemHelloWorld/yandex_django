import django.contrib.auth.models
import django.db.models


class Profile(django.db.models.Model):
    user = django.db.models.OneToOneField(
        django.contrib.auth.models.User,
        on_delete=django.db.models.CASCADE,
        null=False,
        blank=False,
    )

    birthday = django.db.models.DateField(
        null=True, blank=True, verbose_name="дата рождения"
    )

    image = django.db.models.ImageField(
        upload_to="item/main/%Y/%m/%d",
        null=True,
        blank=True,
        verbose_name="аватарка",
    )

    coffe_count = django.db.models.PositiveIntegerField(
        default=0,
        null=False,
        blank=False,
        verbose_name="сколько раз сварил кофе",
    )

    class Meta:
        verbose_name = "Дополнительное поле"
        verbose_name_plural = "Дополнительные поля"
