# Generated by Django 3.1.3 on 2020-11-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_maker', '0003_auto_20201126_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='ytvideos',
            name='ytmage',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]