import django.conf
import django.core.mail
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


def add_feedback_to_db(text, email):
    feedback.models.Feedback.objects.create(text=text, email=email)
