# Generated by Django 4.1.7 on 2023-02-28 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_trips_dates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trips',
            old_name='city',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='trips',
            old_name='country',
            new_name='Country',
        ),
        migrations.RenameField(
            model_name='trips',
            old_name='notes',
            new_name='Notes',
        ),
        migrations.RemoveField(
            model_name='trips',
            name='dates',
        ),
        migrations.AddField(
            model_name='trips',
            name='From',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='trips',
            name='To',
            field=models.DateField(auto_now=True),
        ),
    ]
