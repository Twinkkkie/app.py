from django.shortcuts import render
from .models import Shop

def shops(request):
    shop_info = Shop.objects.order_by('shop_name')
    return render(request, 'shop/shops.html', {'shop_info': shop_info})
