# Generated by Django 3.2.8 on 2021-10-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_exhibition_about_of_exh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='image',
            field=models.ImageField(null=True, upload_to='main/media', verbose_name='Изображение'),
        ),
    ]