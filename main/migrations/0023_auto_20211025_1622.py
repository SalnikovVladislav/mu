# Generated by Django 3.2.8 on 2021-10-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20211025_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibition',
            name='period_time',
        ),
        migrations.AddField(
            model_name='exhibition',
            name='end_time',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='exhibition',
            name='start_time',
            field=models.DateField(null=True),
        ),
    ]
