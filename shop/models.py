from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    ######  Категория товаров  ########
    company = models.CharField(max_length=15)
    in_box = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    ###### Метод вывода категории
    def __str__(self):
        if self.in_box:
            return self.company + ' в коробке'
        else:
            return self.company + ' ключ'

class Item(models.Model):
    ###########  Товары   ##############
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='1')
    title = models.CharField(max_length=100)
    price = models.BigIntegerField()
    retail_price = models.BigIntegerField(default=999999)
    description = models.TextField(max_length=10000)
    pic = models.CharField(max_length=100, default='https://i.ytimg.com/vi/83aci6jpngM/maxresdefault.jpg')
    available = models.BooleanField(default=False)

    def str_id(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return str(self.id)+':' + self.title

    def get_absolute_url(self):
        return reverse('shop:item_page', args=[self.id])

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'price': self.price, 'pic': self.pic}