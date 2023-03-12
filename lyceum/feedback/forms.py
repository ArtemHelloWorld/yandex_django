import django.core.validators
import django.forms
import feedback.models


class FeedbackForm(django.forms.ModelForm):
    email = django.forms.CharField(
        validators=[django.core.validators.validate_email],
        label="Ваша электронная почта",
        help_text="Электронная почта",
    )

    class Meta:
        model = feedback.models.Feedback
        fields = ["email", "text"]

        labels = {
            feedback.models.Feedback.text.field.name: (
                "Напишите всё, что хотите сказать <3"
            ),
        }
        help_texts = {
            feedback.models.Feedback.text.field.name: "Сообщение",
        }
