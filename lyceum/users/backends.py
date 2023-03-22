import django.conf
import django.contrib.auth.backends
import django.contrib.auth.hashers
import django.contrib.auth.models
import users.services


class AuthByEmailBackend(django.contrib.auth.backends.BaseBackend):
    def authenticate(self, request, username=None, password=None):
        email = username
        try:
            user = django.contrib.auth.models.User.objects.get(
                email=users.services.generate_normalize_email(email)
            )
        except django.contrib.auth.models.User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            return django.contrib.auth.models.User.objects.get(pk=user_id)
        except django.contrib.auth.models.User.DoesNotExist:
            return None
