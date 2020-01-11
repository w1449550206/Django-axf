from django.shortcuts import render

# Create your views here.
from Home.models import AxfWheel, AxfNav, AxfMustBuy


def home(request):

    wheels  = AxfWheel.objects.all()
    navs = AxfNav.objects.all()
    mustbuys = AxfMustBuy.objects.all()

    return render(request,'axf/main/home/home.html',context=locals())