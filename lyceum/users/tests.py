import django.contrib.auth.models
import django.core.mail
import django.shortcuts
import django.test
import django.urls
import freezegun
import users.forms
import users.services


class SignUpTests(django.test.TestCase):
    def setUp(self):
        self.client = django.test.Client()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = users.forms.SignUpForm()

    def test_signup_incorrect_password(self):
        count = django.contrib.auth.models.User.objects.count()
        form_data = {
            "username": "testusername",
            "email": "teatmail@mail.ru",
            "password1": "Testpasswordaloalo35aloalo",
            "password2": "testpasswordaloalo35aloalo",
        }
        self.client.post(
            django.shortcuts.reverse("users:signup"),
            data=form_data,
            follow=True,
        )
        self.assertEqual(
            count, django.contrib.auth.models.User.objects.count()
        )

    def test_signup_correct_password(self):
        count = django.contrib.auth.models.User.objects.count()
        form_data = {
            "username": "testusername",
            "email": "teatmail@mail.ru",
            "password1": "Testpasswordaloalo35aloalo",
            "password2": "Testpasswordaloalo35aloalo",
        }
        self.client.post(
            django.shortcuts.reverse("users:signup"),
            data=form_data,
            follow=True,
        )
        self.assertEqual(
            count + 1, django.contrib.auth.models.User.objects.count()
        )

    @django.test.override_settings(ACTIVATE_USERS=True)
    def test_signup_activate_user_true(self):
        form_data = {
            "username": "testusername",
            "email": "teatmail@mail.ru",
            "password1": "Testpasswordaloalo35aloalo",
            "password2": "Testpasswordaloalo35aloalo",
        }
        self.client.post(
            django.shortcuts.reverse("users:signup"),
            data=form_data,
            follow=True,
        )
        self.assertEqual(
            django.contrib.auth.models.User.objects.get(
                username="testusername"
            ).is_active,
            True,
        )

    @django.test.override_settings(ACTIVATE_USERS=False)
    def test_signup_activate_user_false(self):
        form_data = {
            "username": "testusername",
            "email": "teatmail@mail.ru",
            "password1": "Testpasswordaloalo35aloalo",
            "password2": "Testpasswordaloalo35aloalo",
        }
        self.client.post(
            django.shortcuts.reverse("users:signup"),
            data=form_data,
            follow=True,
        )
        self.assertEqual(
            django.contrib.auth.models.User.objects.get(
                username="testusername"
            ).is_active,
            False,
        )

    @django.test.override_settings(ACTIVATE_USERS=False)
    def test_signup_activate_user_false_redirect(self):
        form_data = {
            "username": "testusername",
            "email": "teatmail@mail.ru",
            "password1": "Testpasswordaloalo35aloalo",
            "password2": "Testpasswordaloalo35aloalo",
        }
        response = self.client.post(
            django.shortcuts.reverse("users:signup"),
            data=form_data,
            follow=True,
        )
        self.assertRedirects(
            response, django.shortcuts.redirect("users:signup_complete").url
        )

    @django.test.override_settings(ACTIVATE_USERS=False)
    def test_signup_activate_user_false_mail_send(self):
        form_data = {
            "username": "testusername",
            "email": "teatmail@mail.ru",
            "password1": "Testpasswordaloalo35aloalo",
            "password2": "Testpasswordaloalo35aloalo",
        }
        self.client.post(
            django.shortcuts.reverse("users:signup"),
            data=form_data,
            follow=True,
        )
        self.assertEqual(len(django.core.mail.outbox), 1)

    @freezegun.freeze_time("2023-03-19 00:00:01")
    @django.test.override_settings(ACTIVATE_USERS=False)
    def test_signup_activate_user_false_in_time(self):
        form_data = {
            "username": "testusername",
            "email": "teatmail@mail.ru",
            "password1": "Testpasswordaloalo35aloalo",
            "password2": "Testpasswordaloalo35aloalo",
        }
        self.client.post(
            django.shortcuts.reverse("users:signup"),
            data=form_data,
            follow=True,
        )

        email_body = django.core.mail.outbox[0].body

        with freezegun.freeze_time("2023-03-19 11:30:00"):
            self.client.get(
                django.urls.reverse(
                    "users:signup_activate",
                    kwargs={"activation_code": email_body.split("/")[-1]},
                )
            )

            self.assertEqual(
                django.contrib.auth.models.User.objects.get(
                    username="testusername"
                ).is_active,
                True,
            )

    @freezegun.freeze_time("2023-03-19 00:00:01")
    @django.test.override_settings(ACTIVATE_USERS=False)
    def test_signup_activate_user_false_out_of_time(self):
        form_data = {
            "username": "testusername",
            "email": "teatmail@mail.ru",
            "password1": "Testpasswordaloalo35aloalo",
            "password2": "Testpasswordaloalo35aloalo",
        }
        self.client.post(
            django.shortcuts.reverse("users:signup"),
            data=form_data,
            follow=True,
        )

        email_body = django.core.mail.outbox[0].body

        with freezegun.freeze_time("2023-03-19 12:30:00"):
            self.client.get(
                django.urls.reverse(
                    "users:signup_activate",
                    kwargs={"activation_code": email_body.split("/")[-1]},
                )
            )

            self.assertEqual(
                django.contrib.auth.models.User.objects.get(
                    username="testusername"
                ).is_active,
                False,
            )


class LoginTests(django.test.TestCase):
    def setUp(self):
        form_data_signup = {
            "username": "testusername",
            "email": "teatmail@mail.ru",
            "password1": "Testpasswordaloalo35aloalo",
            "password2": "Testpasswordaloalo35aloalo",
        }

        self.client = django.test.Client()

        self.user = self.client.post(
            django.shortcuts.reverse("users:signup"),
            data=form_data_signup,
            follow=True,
        )

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = users.forms.SignUpForm()

    def test_login_by_username(self):
        form_data_login = {
            "username": "testusername",
            "password": "Testpasswordaloalo35aloalo",
        }

        response = self.client.post(
            django.shortcuts.reverse("users:login"),
            data=form_data_login,
            follow=True,
        )

        self.assertTrue(response.context["user"].is_authenticated)

    def test_login_by_email(self):
        form_data_login = {
            "username": "teatmail@mail.ru",
            "password": "Testpasswordaloalo35aloalo",
        }

        response = self.client.post(
            django.shortcuts.reverse("users:login"),
            data=form_data_login,
            follow=True,
        )

        self.assertTrue(response.context["user"].is_authenticated)

    def test_login_incorrect_username(self):
        form_data = {
            "username": "incorrect",
            "password": "Testpasswordaloalo35aloalo",
        }
        response = self.client.post(
            django.shortcuts.reverse("users:login"),
            data=form_data,
            follow=True,
        )
        self.assertFalse(response.context["user"].is_authenticated)

    def test_login_incorrect_email(self):
        form_data = {
            "username": "incorrct@mail.ru",
            "password": "Testpasswordaloalo35aloalo",
        }
        response = self.client.post(
            django.shortcuts.reverse("users:login"),
            data=form_data,
            follow=True,
        )
        self.assertFalse(response.context["user"].is_authenticated)

    def test_login_incorrect_password(self):
        form_data = {
            "username": "testusername",
            "password": "IncorrctPassword",
        }
        response = self.client.post(
            django.shortcuts.reverse("users:login"),
            data=form_data,
            follow=True,
        )
        self.assertFalse(response.context["user"].is_authenticated)
