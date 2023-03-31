import django.contrib.auth.models
import django.forms.models
import django.shortcuts
import django.test
import django.urls
import freezegun

import users.models


@django.test.override_settings(RATE_LIMIT_MIDDLEWARE=False)
class MyMiddlewareTestCase(django.test.TestCase):
    def setUp(self):
        self.client = django.test.Client()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @django.test.override_settings(RATE_LIMIT_MIDDLEWARE=True)
    @django.test.override_settings(REQUESTS_PER_SECOND=2)
    def test_rate_limit_middleware(self):
        response = self.client.get(
            django.shortcuts.reverse("homepage:homepage")
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            django.shortcuts.reverse("homepage:homepage")
        )
        self.assertEqual(response.status_code, 429)


class BirthdayContextProcessorTest(django.test.TestCase):
    def registrate_user(self):
        form_data_signup = {
            "username": "testusername",
            "email": "testemail@mail.ru",
            "password1": "Testpassword483",
            "password2": "Testpassword483",
        }

        self.user = self.client.post(
            django.shortcuts.reverse("users:signup"),
            data=form_data_signup,
            follow=True,
        )

    @freezegun.freeze_time("2023-01-01 00:00:01")
    def test_birthday_today(self):
        self.registrate_user()

        user_id = django.contrib.auth.models.User.objects.get(
            username="testusername"
        ).id
        profile = users.models.Profile.objects.get(user_id=user_id)
        profile.birthday = "1984-01-01"
        profile.save()

        with freezegun.freeze_time("2023-01-01 00:30:00"):
            response = django.test.Client().get(
                django.urls.reverse("homepage:homepage")
            )
            self.assertNotEqual(len(response.context["BIRTHDAY_PEOPLE"]), 0)

    @freezegun.freeze_time("2023-01-01 00:00:01")
    def test_birthday_not_today(self):
        self.registrate_user()

        user_id = django.contrib.auth.models.User.objects.get(
            username="testusername"
        ).id
        profile = users.models.Profile.objects.get(user_id=user_id)
        profile.birthday = "2023-01-02"
        profile.save()

        with freezegun.freeze_time("2023-01-01 00:30:00"):
            response = django.test.Client().get(
                django.urls.reverse("homepage:homepage")
            )
            self.assertEqual(len(response.context["BIRTHDAY_PEOPLE"]), 0)
