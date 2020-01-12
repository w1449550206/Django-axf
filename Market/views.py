from django.shortcuts import render

# Create your views here.
from Market.models import AxfFoodType


def market(request):

    foodtypes  = AxfFoodType.objects.all()

    context = {
        'foodtypes':foodtypes
    }

    return render(request,'axf/main/market/market.html',context=context)