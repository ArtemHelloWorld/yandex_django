import django.core.validators
import django.forms

import feedback.models


class FeedbackForm(django.forms.Form):
    email = django.forms.EmailField(
        validators=[django.core.validators.validate_email],
        label="Ваша электронная почта",
        help_text="Электронная почта",
    )
    text = django.forms.CharField(
        widget=django.forms.Textarea,
        help_text="Сообщение",
        label="Напишите всё, что хотите сказать <3",
    )
    files = django.forms.FileField(
        widget=django.forms.ClearableFileInput(attrs={"multiple": True}),
        required=False,
        help_text="Файлы",
        label="Добавьте файлы",
    )


class FeedbackCheckForm(django.forms.ModelForm):
    class Meta:
        model = feedback.models.PersonalInformation
        fields = ["email"]

        labels = {"email": "Ваша электронная почта"}

        help_texts = {
            feedback.models.PersonalInformation.email.field.name: (
                "Введите почту, которую вы указывали в форме обратной связи"
            )
        }
