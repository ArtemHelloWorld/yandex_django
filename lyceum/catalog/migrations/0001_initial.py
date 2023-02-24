# Generated by Django 3.2.16 on 2023-02-23 19:22

import catalog.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название. Максимум 150 символов', max_length=150, verbose_name='название')),
                ('name_normalized', models.CharField(editable=False, max_length=200, unique=True)),
                ('is_published', models.BooleanField(default=True, help_text='Уберите галочку, если хотите скрыть запись', verbose_name='опубликовано')),
                ('slug', models.SlugField(help_text='Укажите слаг, который будет отображаться в ссылке', max_length=200, verbose_name='слаг')),
                ('weight', models.PositiveSmallIntegerField(default=100, help_text='Укажите массу', verbose_name='масса')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название. Максимум 150 символов', max_length=150, verbose_name='название')),
                ('name_normalized', models.CharField(editable=False, max_length=200, unique=True)),
                ('is_published', models.BooleanField(default=True, help_text='Уберите галочку, если хотите скрыть запись', verbose_name='опубликовано')),
                ('slug', models.SlugField(help_text='Укажите слаг, который будет отображаться в ссылке', max_length=200, verbose_name='слаг')),
            ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название. Максимум 150 символов', max_length=150, verbose_name='название')),
                ('is_published', models.BooleanField(default=True, help_text='Уберите галочку, если хотите скрыть запись', verbose_name='опубликовано')),
                ('text', models.TextField(help_text='Придумайте описание. Текст должен включать слова превосходно или роскошно', validators=[catalog.validators.ValidateMustContain('превосходно', 'роскошно')], verbose_name='описание')),
                ('category', models.ForeignKey(help_text='Выберите категорию или добавьте новую', on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория')),
                ('tags', models.ManyToManyField(help_text='Выберите тег или создайте новый', to='catalog.Tag', verbose_name='теги')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
    ]
