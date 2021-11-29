# Generated by Django 3.2.9 on 2021-11-27 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20211126_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedtrips',
            name='user_email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='bookedtrips',
            name='user_message',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='bookedtrips',
            name='user_phone',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='bookedtrips',
            name='trip_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
