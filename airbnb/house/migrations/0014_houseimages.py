# Generated by Django 2.0.6 on 2018-07-02 13:54

from django.db import migrations, models
import django.db.models.deletion
import house.models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0013_auto_20180628_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to=house.models.upload_location)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.House')),
            ],
        ),
    ]
