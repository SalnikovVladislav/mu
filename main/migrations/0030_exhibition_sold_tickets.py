# Generated by Django 3.2.8 on 2021-10-25 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_tickets_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='sold_tickets',
            field=models.IntegerField(default=0),
        ),
    ]
