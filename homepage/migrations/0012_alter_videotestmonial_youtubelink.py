# Generated by Django 4.0.3 on 2023-02-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_videotestmonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videotestmonial',
            name='youtubelink',
            field=models.CharField(max_length=50, verbose_name='youtube video code'),
        ),
    ]
