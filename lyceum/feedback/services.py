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
