# Generated by Django 4.0.3 on 2023-03-10 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0018_alter_newsletters_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visasuccess',
            name='discripton',
        ),
        migrations.RemoveField(
            model_name='visasuccess',
            name='title',
        ),
    ]
