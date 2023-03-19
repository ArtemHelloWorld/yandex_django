import django.contrib.auth.forms
import django.contrib.auth.models
import django.forms
import users.models


class UserForm(django.forms.ModelForm):
    class Meta:
        model = django.contrib.auth.models.User
        fields = ["email", "username", "first_name", "last_name"]


class UserProfileForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.readonly:
            self.fields[field].widget.attrs["readonly"] = True

    class Meta:
        model = users.models.Profile
        fields = ("birthday", "image", "coffe_count")

        readonly = ("coffe_count",)


class SignUpForm(django.contrib.auth.forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = django.contrib.auth.models.User
        fields = ("username", "email", "password1", "password2")
        required = ("username", "email", "password1", "password2")
