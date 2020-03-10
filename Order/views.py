from alipay import AliPay
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from Cart.models import AxfCart
from Cart.view_containt import get_total_price
from Order.models import AxfOrder, AxfOrderGoods
from axf.settings import PRIVATE_KEY, PUBLIC_KEY


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


    data= {
        'msg':'ok',
        'status':200,
        'order_id':order.id
    }

    return JsonResponse(data=data)


def orderDetail(request):

    order_id = request.GET.get('order_id')

    order = AxfOrder.objects.get(pk=order_id)

    print(order.id)

    context = {
        'order':order
    }

    return render(request,'axf/order/orderDetail.html',context=context)


def testPay(request):



    alipay = AliPay(
        appid="2016102100728822",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=PRIVATE_KEY,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=PUBLIC_KEY,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug = False  # 默认False
    )

    # 如果你是Python 2用户（考虑考虑升级到Python 3吧），请确保非ascii的字符串为utf8编码：
    # subject = u"测试订单".encode("utf8")
    # 如果你是 Python 3的用户，使用默认的字符串即可
    subject = "苹果耳机"

    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no="110",
        total_amount=1999,
        subject=subject,
        return_url="https://www.1000phone.com",
        notify_url="https://www.1000phone.com"  # 可选, 不填则使用默认notify url
    )


    return redirect('https://openapi.alipaydev.com/gateway.do?' + order_string)