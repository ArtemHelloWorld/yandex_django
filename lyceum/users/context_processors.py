import django.utils.timezone

import users.models


def birthday_people(request):
    return {
        "BIRTHDAY_PEOPLE": users.models.MyUser.objects.filter(
            profile__birthday=django.utils.timezone.localdate()
        ).values("username", "email")
    }
