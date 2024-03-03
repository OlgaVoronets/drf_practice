
from django.db import models

from config import settings
from services import convert_currency

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Порода')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='Кличка')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Порода')
    photo = models.ImageField(upload_to='dogs/', **NULLABLE,
                              verbose_name='Фото')
    birth_day = models.DateField(**NULLABLE, verbose_name='Дата рождения')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              **NULLABLE, verbose_name='Владелец')
    is_public = models.BooleanField(default=False, verbose_name='статус')
    price = models.PositiveIntegerField(**NULLABLE, verbose_name='цена, руб')

    def __str_(self):
        return f'{self.name} ({self.category})'

    @property
    def price_usd(self):
        return convert_currency(self.price, 'usd')

    @property
    def price_eur(self):
        return convert_currency(self.price, 'eur')

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'




