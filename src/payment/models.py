from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Item(models.Model):
    name: models.CharField = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description:models.CharField = models.CharField(
        max_length=300,
        verbose_name='Описание'
    )
    price:models.IntegerField = models.IntegerField(verbose_name='Цена')
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self) -> str:
        return reverse('item', kwargs={'id' : self.pk})
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    
class Order(models.Model):
    user: models.ForeignKey = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    item: models.ForeignKey = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )
    
    def __repr__(self) -> str:
        return str(self.user) + '_' + str(self.item)
    
    class Meta:
        verbose_name = 'Заказ'