# Generated by Django 3.2.16 on 2023-03-06 18:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_itemimagegallery_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения'),
        ),
    ]
