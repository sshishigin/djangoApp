from django.db import models

from users.models import User


class Category(models.Model):
    company = models.CharField(max_length=15)
    in_box = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        if self.in_box:
            return self.company + ' в коробке'
        else:
            return self.company + ' ключ'


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='1')
    title = models.CharField(max_length=100)
    price = models.BigIntegerField(default=0)
    retail_price = models.BigIntegerField(default=999999)
    description = models.TextField(max_length=10000)
    pic = models.CharField(max_length=130, default='https://images.pexels.com/photos/1666067/pexels-photo-1666067.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260')
    available = models.BooleanField(default=False)
    users = models.ManyToManyField(User, through='UserItemRelation')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"{self.title} (Id:{self.id})"

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'price': self.price, 'pic': self.pic}


class UserItemRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    like = models.BooleanField(default=False)
