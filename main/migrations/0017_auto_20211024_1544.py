# Generated by Django 3.2.8 on 2021-10-24 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20211024_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exhibition',
            old_name='end_time',
            new_name='end_time_1',
        ),
        migrations.RenameField(
            model_name='exhibition',
            old_name='start_time',
            new_name='start_time_1',
        ),
    ]
