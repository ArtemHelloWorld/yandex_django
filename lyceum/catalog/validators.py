import django.core.exceptions


def exist_adverbs_validator(value):
    if not ("превосходно" in value.lower() or "роскошно" in value.lower()):
        raise django.core.exceptions.ValidationError(
            "Не содержит наречий. Добавьте `превосходно` или `роскошно`"
        )
