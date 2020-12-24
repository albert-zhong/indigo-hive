# Generated by Django 3.1.4 on 2020-12-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(default='slug', max_length=63, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(default='slug', max_length=63, unique=True),
            preserve_default=False,
        ),
    ]
