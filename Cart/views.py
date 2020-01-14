from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from Cart.models import AxfCart


def cart(request):


    # 当前用户的购物车

    user_id = request.session.get('user_id')

    carts = AxfCart.objects.filter(c_user_id=user_id)

    context = {
        'carts':carts
    }

    return render(request,'axf/main/cart/cart.html',context=context)


def addToCart(request):

    goodsid = request.GET.get('goodsid')

    # 如果获取到了goodsid  那么我们还需要user的id
    # 如果购物车中没有该数据 那么就添加  如果有之前的商品了 那么数量加一

    user_id = request.session.get('user_id')

    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_goods_id=goodsid)

    if carts.exists():
        cart = carts.first()
        cart.c_goods_num = cart.c_goods_num + 1

    else:
        cart = AxfCart()
        cart.c_user_id = user_id
        cart.c_goods_id = goodsid
        #
        # cart.c_user = AxfUser.objects.get(pk=user_id)
        # cart.c_goods= AxfGoods.objects.get(pk=goodsid)

    cart.save()

    data = {
        'status':200,
        'msg':'ok',
        'c_goods_num':cart.c_goods_num
    }

    return JsonResponse(data=data)