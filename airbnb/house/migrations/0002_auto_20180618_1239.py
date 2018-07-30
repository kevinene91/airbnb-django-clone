# Generated by Django 2.0.6 on 2018-06-18 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='user',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='house',
            name='mod_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='house',
            name='no_baths',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='house',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='shared_spaces',
            field=models.CharField(choices=[('KITHCHEN', 'KITHCHEN'), ('LAUNDRY', 'KITHCHEN'), ('POOL', 'POOL'), ('GYM', 'GYM'), ('PARKING', 'PARKING')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='slug',
            field=models.CharField(default='house', max_length=253, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='house',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='no_bedrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='house',
            name='no_beds',
            field=models.IntegerField(default=0),
        ),
    ]
