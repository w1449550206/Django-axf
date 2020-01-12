from django.shortcuts import render

# Create your views here.
from Market.models import AxfFoodType, AxfGoods


def market(request):

    foodtypes = AxfFoodType.objects.all()

    goods_list = AxfGoods.objects.all()[0:5]


    context = {
        'foodtypes':foodtypes,
        'goods_list':goods_list,
    }


    return render(request,'axf/main/market/market.html',context=context)