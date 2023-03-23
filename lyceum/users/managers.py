import django.db.models


class MyUserManager(django.db.models.Manager):
    def get_queryset(self):
        return (
            super(MyUserManager, self).get_queryset().select_related("profile").filter(is_active=True)
        )
