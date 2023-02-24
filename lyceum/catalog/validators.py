import re

import django.core.exceptions
import django.utils.deconstruct

PATTERN = re.compile(r"\w+|\W+")


@django.utils.deconstruct.deconstructible
class ValidateMustContain:
    def __init__(self, *words):
        self.words = words

    def __call__(self, value):
        value_set = set(re.findall(PATTERN, value.lower()))
        if not (value_set & set(self.words)):
            raise django.core.exceptions.ValidationError(
                f"Не содержит наречий."
                f" Добавьте {', '.join([word for word in self.words])}"
            )
