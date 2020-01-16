from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from Cart.models import AxfCart
from Cart.view_containt import get_total_price
from Order.models import AxfOrder, AxfOrderGoods


@csrf_exempt
def makeOrder(request):
    # 在订单的页面 应该展示的是ordergoods的数据
    # ordergoods依赖于order
    # order依赖于user

    user_id = request.session.get('user_id')

    # user_id = request.user_id

    order = AxfOrder()
    order.o_user_id = user_id
    order.o_price = get_total_price(user_id)
    order.save()

    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)

    for cart in carts:
        ordergoods = AxfOrderGoods()

        ordergoods.og_order = order

        ordergoods.og_goods = cart.c_goods

        ordergoods.og_num = cart.c_goods_num

        ordergoods.save()

        cart.delete()

    data = {
        'msg': 'ok',
        'status': 200,
        'order_id': order.id
    }

    return JsonResponse(data=data)


def orderDetail(request):
    order_id = request.GET.get('order_id')

    order = AxfOrder.objects.get(pk=order_id)

    print(order.id)

    context = {
        'order': order
    }

    return render(request, 'axf/order/orderDetail.html', context=context)
