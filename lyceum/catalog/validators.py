import re

import django.core.exceptions


class ValidateMustContain:
    def __init__(self, *words):
        self.words = words

    def __call__(self, value):
        value_set = set(re.findall(re.compile(r"\w+|\W+"), value.lower()))
        if not (value_set & set(self.words)):
            raise django.core.exceptions.ValidationError(
                f"Не содержит наречий."
                f" Добавьте {', '.join([word for word in self.words])}"
            )
