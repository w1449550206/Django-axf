from Cart.models import AxfCart


def get_total_price(user_id):
    # 当前用户购买的所有产品
    carts=AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)
    total_price = 0
    for cart in carts:
        total_price  = total_price + cart.c_goods_num * cart.c_goods.price
    return '%.2f' %total_price
