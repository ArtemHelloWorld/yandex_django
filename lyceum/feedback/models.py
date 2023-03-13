import django.db.models


class Feedback(django.db.models.Model):
    RECEIVED = "received"
    HANDLING = "handling"
    ANSWERED = "answered"

    STATUS_CHOICES = [
        (RECEIVED, "Получено"),
        (HANDLING, "В обработке"),
        (ANSWERED, "Ответ дан"),
    ]
    text = django.db.models.TextField(verbose_name="Сообщение пользователя")
    email = django.db.models.EmailField(
        verbose_name="Почта пользователя, оставившего сообщение"
    )
    status = django.db.models.CharField(
        choices=STATUS_CHOICES,
        max_length=8,
        default=RECEIVED,
        verbose_name="Статус обработки",
    )
    created_on = django.db.models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания"
    )

    class Meta:
        verbose_name = "сообщение пользователя"
        verbose_name_plural = "сообщения пользователей"
