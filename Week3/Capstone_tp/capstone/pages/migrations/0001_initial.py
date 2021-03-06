# Generated by Django 4.1.dev20211104192835 on 2021-11-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('question1', models.CharField(max_length=200)),
                ('question2', models.CharField(max_length=200)),
                ('question3', models.CharField(max_length=200)),
                ('saved_trips', models.CharField(max_length=200)),
                ('booked_trips', models.CharField(max_length=200)),
                ('reviews', models.CharField(max_length=200)),
                ('time_stamp', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
