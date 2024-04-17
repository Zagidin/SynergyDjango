from django.db import models


class Category(models.Model):
    name = models.CharField("Категория", max_length=45, default='Новый товар')
    description = models.TextField("Описание")
    
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Категория_Товара'
        verbose_name_plural = 'Категория_Товаров'
        
    
class Manufacturer(models.Model):
    title = models.CharField("Бренд", max_length=35, default='Нет Бренда')
    description = models.TextField("Описание")
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Производитель_Товара'
        verbose_name_plural = 'Производитель_Товаров'
