# Generated by Django 2.0.6 on 2018-06-21 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_auto_20180621_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='slug',
        ),
    ]
