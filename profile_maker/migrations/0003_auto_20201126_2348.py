# Generated by Django 3.1.3 on 2020-11-26 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_maker', '0002_ytvideos'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypeople',
            name='pmage',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ytvideos',
            name='ylink',
            field=models.URLField(),
        ),
    ]
