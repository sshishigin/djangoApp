from django.db import models

from users.models import CustomUser


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
    pic = models.CharField(max_length=100, default='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.dribbble.com%2Fusers%2F448879%2Fscreenshots%2F2487655%2Faguacate.jpg&f=1&nofb=1')
    available = models.BooleanField(default=False)

    def str_id(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return str(self.id)+':' + self.title

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'price': self.price, 'pic': self.pic}


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, default=None)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
