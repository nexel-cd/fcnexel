# Generated by Django 4.0.3 on 2023-02-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_universities'),
    ]

    operations = [
        migrations.AddField(
            model_name='universities',
            name='collegeimage',
            field=models.ImageField(blank=True, null=True, upload_to='universityImage'),
        ),
    ]
