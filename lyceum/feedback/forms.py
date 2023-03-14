import django.core.validators
import django.forms


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
