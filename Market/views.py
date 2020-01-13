from django.shortcuts import render

# Create your views here.
from Market.models import AxfFoodType, AxfGoods
from Market.view_helper import COM_SORT_RULE, ORDER_BY_PRICE_UP, ORDER_BY_PRICE_DOWN, ORDER_BY_NUM_UP, ORDER_BY_NUM_DOWN


def market(request):

    foodtypes = AxfFoodType.objects.all()


    # 获取商品的类别
    typeid = request.GET.get('typeid','104749')

    # 获取typeid对应的全部类别
    childtypenames = AxfFoodType.objects.filter(typeid=typeid)[0].childtypenames

    # 将类别进行切割 提取列表
    childtypename_list = childtypenames.split('#')

    cname_list = []

    for childtypename in childtypename_list:
        cname = childtypename.split(':')
        cname_list.append(cname)


    goods_list = AxfGoods.objects.filter(categoryid=typeid)

    childcid = request.GET.get('childcid','0')


    # childcid中 没有0的值  如果没有0的值 我们就是查询的所有  有一个非0的值 那么才会进行二次查询
    if childcid == '0':
        pass
    else:
        goods_list = goods_list.filter(childcid=childcid)


    sort_rule_list = [
        ['综合排序',COM_SORT_RULE],
        ['价格升序',ORDER_BY_PRICE_UP],
        ['价格降序',ORDER_BY_PRICE_DOWN],
        ['销量升序',ORDER_BY_NUM_UP],
        ['销量降序',ORDER_BY_NUM_DOWN],
    ]


    rule = request.GET.get('rule','0')

    if rule == COM_SORT_RULE:
        pass
    elif rule == ORDER_BY_PRICE_UP:
        goods_list = goods_list.order_by('price')
    elif rule == ORDER_BY_PRICE_DOWN:
        goods_list = goods_list.order_by('-price')
    elif rule == ORDER_BY_NUM_UP:
        goods_list = goods_list.order_by('productnum')
    elif rule == ORDER_BY_NUM_DOWN:
        goods_list = goods_list.order_by('-productnum')




    context = {
        'foodtypes':foodtypes,
        'goods_list':goods_list,
        'typeid':typeid,
        'cname_list':cname_list,
        'childcid':childcid,
        'sort_rule_list':sort_rule_list,
        'rule':rule
    }


    return render(request,'axf/main/market/market.html',context=context)