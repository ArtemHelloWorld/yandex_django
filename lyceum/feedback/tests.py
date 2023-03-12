import django.test
import django.urls
import django.shortcuts
import feedback.forms

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
        email_label = self.form.fields['email'].label
        self.assertEqual(
            email_label,
            'Ваша электронная почта'
        )

    def test_email_help_text(self):
        email_help_text = self.form.fields['email'].help_text
        self.assertEqual(
            email_help_text,
            'Электронная почта'
        )

    def test_text_label(self):
        text_label = self.form.fields['text'].label
        self.assertEqual(
            text_label,
            'Напишите всё, что хотите сказать <3'
        )

    def test_text_help_text(self):
        text_help_text = self.form.fields['text'].help_text
        self.assertEqual(
            text_help_text,
            'Сообщение'
        )

    def test_feedback_redirect(self):
        form_data = {
            'text': 'Мои возмущения',
            'email': 'mailmail@mail.ru'
        }
        response = self.client.post(
            django.shortcuts.reverse('feedback:feedback'),
            data=form_data,
            follow=True
        )
        self.assertRedirects(response, django.shortcuts.reverse('feedback:feedback'))
