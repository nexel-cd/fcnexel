# Generated by Django 4.0.3 on 2023-02-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='universities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='University Name')),
                ('Course', models.CharField(max_length=250, verbose_name='Course')),
                ('country', models.CharField(max_length=150, verbose_name='Country')),
                ('state', models.CharField(max_length=150, verbose_name='State')),
                ('los', models.CharField(choices=[('PG', 'PG'), ('UG', 'UG')], max_length=150, verbose_name='Level of Study')),
                ('duraction', models.CharField(max_length=150, verbose_name='Duration')),
            ],
        ),
    ]