import cryptography.fernet
import django.conf
import django.core.mail
import django.db.models
import django.db.models.functions
import feedback.models

MESSAGE = (
    "Спасибо за ваш отзыв!\n"
    "Мы получили выше обращение "
    "через форму обратной связи "
    "со следующим сообщением:\n"
    "{}\n"
    "В ближайшее время мы рассмотрим "
    "ваше обращение и отправим письмо "
    "с ответом!"
)


def send_feedback_mail(text, email):
    django.core.mail.send_mail(
        subject="Subject",
        message=MESSAGE.format(text),
        from_email=django.conf.settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
    )


def add_feedback_to_db(text, email, files):
    personal_information = feedback.models.PersonalInformation.objects.create(
        email=email
    )

    fb = feedback.models.Feedback.objects.create(
        text=text, personal_information=personal_information
    )
    for file in files:
        feedback.models.FeedbackFile.objects.create(feedback=fb, file=file)


def get_feedbacks_by_email(email):
    feedbacks = feedback.models.Feedback.objects.filter(
        personal_information__email=email
    ).only(
        "status",
        "created_on",
    )
    return feedbacks


def decode_item_id(encoded_id):
    f = cryptography.fernet.Fernet(django.conf.settings.KEY32)
    encrypt = f.decrypt(encoded_id)
    return int(encrypt)


def get_feedback_by_pk(pk):
    feedback_item = (
        feedback.models.Feedback.objects.prefetch_related(
            django.db.models.Prefetch(
                "files",
                queryset=feedback.models.FeedbackFile.objects.all().only(
                    "file"
                ),
            )
        )
        .only("text", "status", "created_on")
        .filter(pk=decode_item_id(pk))
        .first()
    )

    return feedback_item
