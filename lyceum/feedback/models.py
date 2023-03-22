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
    status = django.db.models.CharField(
        choices=STATUS_CHOICES,
        max_length=8,
        default=RECEIVED,
        verbose_name="Статус обработки",
    )
    personal_information = django.db.models.OneToOneField(
        "PersonalInformation",
        on_delete=django.db.models.CASCADE,
        related_name="personal_information",
    )
    created_on = django.db.models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания"
    )

    class Meta:
        verbose_name = "сообщение пользователя"
        verbose_name_plural = "сообщения пользователей"


def feedback_upload_path(instance, filename):
    return f"uploads/{instance.feedback.id}/{filename}"


class FeedbackFile(django.db.models.Model):
    feedback = django.db.models.ForeignKey(
        Feedback, on_delete=django.db.models.CASCADE, related_name="files"
    )
    file = django.db.models.FileField(
        upload_to=feedback_upload_path,
    )


class PersonalInformation(django.db.models.Model):
    email = django.db.models.EmailField(
        verbose_name="Почта пользователя, оставившего сообщение"
    )
