# Generated by Django 2.0.6 on 2018-07-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180710_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='adress',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
