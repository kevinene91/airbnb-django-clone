# Generated by Django 2.0.6 on 2018-07-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180710_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
