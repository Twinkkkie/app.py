from django.db import models

class Shop(models.Model):
    shop_name = models.CharField('Название', max_length=250)
    address = models.CharField('Адрес', max_length=250)
    description = models.TextField('Описание услуг')

    def str(self):
        return self.shop_name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
