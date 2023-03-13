import django.shortcuts
import django.test
import django.urls
import feedback.forms
import feedback.models


class ContextTests(django.test.TestCase):
    def setUp(self):
        self.client = django.test.Client()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = feedback.forms.FeedbackForm()

    def test_feedback_context(self):
        response = self.client.get(django.urls.reverse("feedback:feedback"))
        self.assertIn("form", response.context)

    def test_email_label(self):
        email_label = self.form.fields["email"].label
        self.assertEqual(email_label.lower(), "ваша электронная почта")

    def test_email_help_text(self):
        email_help_text = self.form.fields["email"].help_text
        self.assertEqual(email_help_text.lower(), "электронная почта")

    def test_text_label(self):
        text_label = self.form.fields["text"].label
        self.assertEqual(
            text_label.lower(), "напишите всё, что хотите сказать <3"
        )

    def test_text_help_text(self):
        text_help_text = self.form.fields["text"].help_text
        self.assertEqual(text_help_text.lower(), "сообщение")

    def test_feedback_redirect(self):
        form_data = {"text": "Мои возмущения", "email": "mailmail@mail.ru"}
        response = self.client.post(
            django.shortcuts.reverse("feedback:feedback"),
            data=form_data,
            follow=True,
        )
        self.assertRedirects(
            response, django.shortcuts.reverse("feedback:feedback")
        )

    def test_feedback_model_added(self):
        form_data = {"text": "Мои возмущения", "email": "mailmail@mail.ru"}
        count = feedback.models.Feedback.objects.all().count()
        self.client.post(
            django.shortcuts.reverse("feedback:feedback"),
            data=form_data,
            follow=True,
        )
        self.assertEqual(
            feedback.models.Feedback.objects.all().count(), count + 1
        )
