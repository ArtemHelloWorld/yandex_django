import datetime

import django.conf
import django.contrib.auth.models
import django.core.mail
import django.core.signing
import django.urls


MESSAGE = "Для завершения регистрации перейдите по ссылке:\n" "{}"


def send_email_with_registration_link(request, user):
    django.core.mail.send_mail(
        subject="Subject",
        message=MESSAGE.format(
            request.build_absolute_uri(generate_activation_link(user))
        ),
        from_email=django.conf.settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )


def generate_activation_link(user):
    signer = django.core.signing.TimestampSigner()
    activation_code = signer.sign(user.username)

    link = django.urls.reverse(
        "users:signup_activate", kwargs={"activation_code": activation_code}
    )
    return link


def validate_activation_link(value):
    signer = django.core.signing.TimestampSigner()
    max_age = datetime.timedelta(hours=12)

    try:
        username = signer.unsign(value, max_age=max_age)
    except Exception:
        return None

    user = django.contrib.auth.models.User.objects.get(username=username)
    return user
