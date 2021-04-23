from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.models import Cart
# from users.models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def order_create(request):
    cart = Cart(request)
    if cart:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                order.user = request.user
                for item in cart:
                    OrderItem.objects.create(order=order,
                                            product=item['item'],
                                            price=item['price'],
                                            quantity=item['quantity'])
                # очистка корзины
                cart.clear()
                send_mail(
                "Подтверждение заказа" , #Тема
                "{name},ваш заказ номер {id} находится в обработке".format(name=order.first_name, id=order.id), #сообщение
                settings.EMAIL_HOST_USER , #адресант
                [order.email], #адресат
                fail_silently = False
                )
                return render(request, 'orders/created.html',
                            {'order': order})
        else:
            form = OrderCreateForm
        return render(request, 'orders/create.html',
                    {'cart': cart, 'form': form})
    else:
        return render(request, 'shop/index.html')