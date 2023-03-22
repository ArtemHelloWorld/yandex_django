import django.conf
import django.contrib.auth.forms
import django.contrib.auth.models
import django.forms
import users.models


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

        if django.contrib.auth.models.User.objects.filter(
            email=email
        ).exists():
            print('1')
            raise django.forms.ValidationError("Такая почта уже существует")

        return email

    class Meta:
        model = django.contrib.auth.models.User
        fields = ("username", "email", "password1", "password2")
        required = ("username", "email", "password1", "password2")


class CustomAuthenticationForm(django.contrib.auth.forms.AuthenticationForm):
    username = django.forms.CharField(label="Логин или почта", max_length=254)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        print(password)
        if username is not None and password:
            # ЭТО БЫЛО ДЛЯ ВТОРОГО ЗАДАНИЯ
            # СЕЙЧАС УЖЕ СДЕЛАЛ КАСТОМНЫЙ БЭКЕНД
            # if '@' in username:
            #     user = django.contrib.auth.models.User.objects.only(
            #         'username'
            #     ).filter(
            #         email=username
            #     ).first()
            #
            #     if not user:
            #         raise django.forms.ValidationError(
            #         'Такой почты нет в базе'
            #         )
            #
            #     username = user.username

            self.user_cache = django.contrib.auth.authenticate(
                self.request, username=username, password=password
            )

            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
