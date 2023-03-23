import django.db.models


class MyUserManager(django.db.models.Manager):
    def get_queryset(self):
        return (
            super(MyUserManager, self).get_queryset().select_related("profile")
        )

    def active(self):
        return self.get_queryset().filter(is_active=True)
