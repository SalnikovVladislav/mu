from django.db import models
from django.forms import ModelForm, ValidationError
from django.contrib.auth.models import User


class Exhibition(models.Model):
    name_of_exh = models.CharField(max_length=32, verbose_name='Название выставки')
    about_of_exh = models.TextField(max_length=420, verbose_name='Об выставке')
    start_time = models.DateField(null=True)
    end_time = models.DateField(null=True)
    image = models.ImageField(verbose_name='Изображение', null=True)
    published = models.DateField(auto_now=True)
    places = models.IntegerField(verbose_name="Всего мест", default=1)
    sold_tickets = models.IntegerField(default=0)

    def __str__(self):
        return self.name_of_exh

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'


class Tickets(models.Model):
    name = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_ticket = models.IntegerField()

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

