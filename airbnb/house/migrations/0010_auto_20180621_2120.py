# Generated by Django 2.0.6 on 2018-06-21 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0009_auto_20180621_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amenities',
            name='mod_date',
        ),
        migrations.RemoveField(
            model_name='amenities',
            name='pub_date',
        ),
    ]