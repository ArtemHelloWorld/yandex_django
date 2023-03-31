import django.utils.timezone

import users.models


def birthday_people(request):
    return {
        "BIRTHDAY_PEOPLE": users.models.MyUser.objects.filter(
            profile__birthday__month=django.utils.timezone.localdate().month,
            profile__birthday__day=django.utils.timezone.localdate().day,
        ).values("username", "email")
    }
