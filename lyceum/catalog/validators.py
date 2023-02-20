import django.core.exceptions


class ValidateMustContain:
    def __init__(self, *words):
        self.words = words

    def __call__(self, value):
        for word in self.words:
            if word.lower() in value.lower():
                return True
        raise django.core.exceptions.ValidationError(
            "Не содержит наречий. Добавьте `превосходно` или `роскошно`"
        )
