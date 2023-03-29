# Generated by Django 3.2.16 on 2023-03-29 11:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MyUser",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("auth.user",),
        ),
        migrations.AlterModelOptions(
            name="profile",
            options={
                "verbose_name": "дополнительное поле",
                "verbose_name_plural": "дополнительные поля",
            },
        ),
    ]
