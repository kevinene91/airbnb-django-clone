# Generated by Django 2.0.6 on 2018-06-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0006_remove_house_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='slug',
            field=models.SlugField(blank=True, max_length=253, unique=True),
        ),
    ]