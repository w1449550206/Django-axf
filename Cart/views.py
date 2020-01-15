from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from Cart.models import AxfCart


def cart(request):


    # 当前用户的购物车

    user_id = request.session.get('user_id')

    carts = AxfCart.objects.filter(c_user_id=user_id)

    # 判断数据库中的选中状态  是否为全选
    is_all_select = not AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=False).exists()


    context = {
        'carts':carts,
        'is_all_select':is_all_select,
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

@csrf_exempt
def subToCart(request):

    cartid = request.POST.get('cartid')

    cart = AxfCart.objects.get(pk=cartid)

    num = cart.c_goods_num

    data = {
        'msg': 'ok',
        'status': 200,
    }

    if num == 1:
        cart.delete()

    else:
        cart.c_goods_num = cart.c_goods_num - 1
        cart.save()
        data['c_goods_num']=cart.c_goods_num




    return JsonResponse(data=data)


def changeStatus(request):

    cartid = request.GET.get('cartid')

    cart = AxfCart.objects.get(pk=cartid)

    cart.c_is_select = not cart.c_is_select

    cart.save()


    user_id = request.session.get('user_id')


    # 在点击修改选中状态之后 再次去判断了  数据库中 是否购物车中的数据全部选中
    is_all_select = not AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=False).exists()


    data={
        'msg':'ok',
        'status':200,
        'c_is_select':cart.c_is_select,
        'is_all_select':is_all_select,
    }
    return JsonResponse(data=data)


def allSelect(request):


    cartlist = request.GET.get('cartlist')

    # ['13', '14', '15']
    cartid_list = cartlist.split('#')

    # 将当前用户的购物车中的在cartid_list中的数据 的c_is_select的值取反

    cart_list = AxfCart.objects.filter(id__in=cartid_list)

    for cart in cart_list:
        cart.c_is_select = not cart.c_is_select
        cart.save()
    data = {
        'msg': 'ok',
        'status': 200,
    }

    return JsonResponse(data=data)