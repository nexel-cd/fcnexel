# Generated by Django 4.0.3 on 2023-02-14 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_universities_collegeimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250, verbose_name='Question')),
                ('answer', models.CharField(max_length=550, verbose_name='Question')),
            ],
        ),
        migrations.CreateModel(
            name='mainregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=250, verbose_name='Last Name')),
                ('email', models.CharField(max_length=250, verbose_name='Email')),
                ('question', models.CharField(max_length=250, verbose_name='Question')),
                ('prefferedstudy', models.CharField(max_length=250, verbose_name='Preffered Study')),
                ('prefferedstudyyear', models.CharField(max_length=250, verbose_name='Preffered Study Year')),
                ('prefferedstudyintake', models.CharField(max_length=250, verbose_name='Preffered study intake')),
                ('message', models.CharField(max_length=250, verbose_name='Any Message')),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('email', models.CharField(max_length=250, verbose_name='Email')),
                ('phono', models.CharField(max_length=250, verbose_name='Phono')),
                ('subject', models.CharField(max_length=250, verbose_name='Subject')),
                ('message', models.CharField(max_length=250, verbose_name='Message')),
            ],
        ),
    ]
