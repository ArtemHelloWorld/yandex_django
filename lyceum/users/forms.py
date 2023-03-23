import django.conf
import django.contrib.auth.forms
import django.contrib.auth.models
import django.forms
import users.models
import users.services


class UserForm(django.forms.ModelForm):
    class Meta:
        model = django.contrib.auth.models.User
        fields = ("email", "username", "first_name", "last_name")


class UserProfileForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.readonly:
            self.fields[field].widget.attrs["readonly"] = True

    class Meta:
        model = users.models.Profile
        fields = ("birthday", "image", "coffee_count")

        readonly = ("coffee_count",)


class SignUpForm(django.contrib.auth.forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if django.contrib.auth.models.User.objects.filter(
            username=username
        ).exists():
            raise django.forms.ValidationError("Такое имя уже существует")

        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")

        normalized_email = users.services.generate_normalize_email(email)

        if django.contrib.auth.models.User.objects.filter(
            email=normalized_email
        ).exists():
            raise django.forms.ValidationError("Такая почта уже существует")

        return normalized_email

    class Meta:
        model = django.contrib.auth.models.User
        fields = ("username", "email", "password1", "password2")
        required = ("username", "email", "password1", "password2")


class CustomAuthenticationForm(django.contrib.auth.forms.AuthenticationForm):
    username = django.forms.CharField(label="Логин или почта", max_length=254)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = django.contrib.auth.authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                count = self.request.session.get("load_count", 0) + 1
                self.request.session["load_count"] = count

                if count == django.conf.settings.MAX_FAILED_LOGIN_ATTEMPTS:
                    self.request.session["load_count"] = 0
                    try:
                        if "@" in username:
                            user = django.contrib.auth.models.User.objects.get(
                                email=users.services.generate_normalize_email(
                                    username
                                )
                            )
                        else:
                            user = django.contrib.auth.models.User.objects.get(
                                username=username
                            )

                        user.is_active = False
                        user.save()

                        users.services.send_email_with_activation_link(
                            self.request, user, activation_back=True
                        )

                        raise django.forms.ValidationError(
                            "Вы превысили количество попыток войти. "
                            "На вашу почту отправлено письмо "
                            "cо ссылкой для восстановления аккаунта"
                        )
                    except django.contrib.auth.models.User.DoesNotExist:
                        raise django.forms.ValidationError(
                            "Вы превысили количество попыток войти."
                        )

                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

                if "load_count" in self.request.session:
                    self.request.session["load_count"] = 0

        return self.cleaned_data
