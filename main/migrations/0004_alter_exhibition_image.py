# Generated by Django 3.2.8 on 2021-10-18 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211018_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='image',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Изображение'),
        ),
    ]
