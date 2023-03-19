# Generated by Django 3.2.16 on 2023-03-13 17:11

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("feedback", "0002_auto_20230313_1417"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonalInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        verbose_name=(
                            "Почта пользователя, " "оставившего сообщение"
                        ),
                    ),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="feedback",
            options={
                "verbose_name": "сообщение пользователя",
                "verbose_name_plural": "сообщения пользователей",
            },
        ),
        migrations.RemoveField(
            model_name="feedback",
            name="email",
        ),
        migrations.CreateModel(
            name="FeedbackFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="uploads/FEEDBACK_ID/")),
                (
                    "feedback",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="feedback.feedback",
                    ),
                ),
            ],
        ),
    ]