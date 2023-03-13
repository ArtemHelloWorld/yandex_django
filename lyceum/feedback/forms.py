import django.core.validators
import django.forms
import feedback.models


class FeedbackForm(django.forms.ModelForm):
    class Meta:
        model = feedback.models.Feedback
        fields = ["email", "text"]

        labels = {
            feedback.models.Feedback.text.field.name: (
                "Напишите всё, что хотите сказать <3"
            ),
            feedback.models.Feedback.email.field.name: (
                "Ваша электронная почта"
            ),
        }

        help_texts = {
            feedback.models.Feedback.text.field.name: "Сообщение",
            feedback.models.Feedback.email.field.name: "Электронная почта",
        }

        validators = {
            feedback.models.Feedback.email.field.name: [
                django.core.validators.validate_email
            ]
        }
