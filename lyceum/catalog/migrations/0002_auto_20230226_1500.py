# Generated by Django 3.2.16 on 2023-02-26 12:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial_squashed_0005_alter_item_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="itemimagegallery",
            options={
                "verbose_name": "фото галерея",
                "verbose_name_plural": "фото галерея",
            },
        ),
        migrations.AlterModelOptions(
            name="itemimagemain",
            options={
                "verbose_name": "фото главное",
                "verbose_name_plural": "фото главные",
            },
        ),
    ]
