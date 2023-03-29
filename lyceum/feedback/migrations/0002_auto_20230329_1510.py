# Generated by Django 3.2.16 on 2023-03-29 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feedback", "0001_initial_squashed_0005_auto_20230318_2038"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="дата и время создания"
            ),
        ),
        migrations.AlterField(
            model_name="feedback",
            name="status",
            field=models.CharField(
                choices=[
                    ("received", "Получено"),
                    ("handling", "В обработке"),
                    ("answered", "Ответ дан"),
                ],
                default="received",
                max_length=8,
                verbose_name="статус обработки",
            ),
        ),
        migrations.AlterField(
            model_name="personalinformation",
            name="email",
            field=models.EmailField(
                max_length=254,
                verbose_name="почта пользователя, оставившего сообщение",
            ),
        ),
    ]