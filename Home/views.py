from django.shortcuts import render

# Create your views here.
from Home.models import AxfWheel


def home(request):

    wheels  =AxfWheel.objects.all()

    return render(request,'axf/main/home/home.html',context=locals())