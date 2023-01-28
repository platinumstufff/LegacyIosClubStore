# Generated by Django 4.1.5 on 2023-01-28 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('name', models.CharField(default='App', help_text='Укажите название приложения', max_length=100)),
                ('app_id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(default='Dev', help_text='Введите разработчика', max_length=50)),
                ('description', models.TextField(default='Ничего', help_text='Введите описание приложения')),
                ('link', models.CharField(default='APP.APK', help_text='Укажите путь к приложению', max_length=300)),
                ('image', models.CharField(default='noimage.png', help_text='Укажите путь к картинке (noimage.png стандартная картинка)', max_length=300)),
                ('platform', models.CharField(choices=[('OS', (('Windows', 'Windows'), ('Android', 'Android'), ('Linux', 'Linux')))], default=None, help_text='Укажите платформу', max_length=300)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('app_id',),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('title', models.CharField(default='Чета случилось', help_text='Введите название новости', max_length=100)),
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(default='Стор удалён, пон.', help_text='Введите текст новости')),
                ('date', models.DateField(default=datetime.date.today, help_text='Укажите дату новости', verbose_name='Date')),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('news_id',),
            },
        ),
    ]
