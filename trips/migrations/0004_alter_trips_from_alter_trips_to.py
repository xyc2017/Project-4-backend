# Generated by Django 4.1.7 on 2023-03-01 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_rename_city_trips_city_rename_country_trips_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='From',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trips',
            name='To',
            field=models.DateField(),
        ),
    ]