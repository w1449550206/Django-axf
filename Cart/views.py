from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def cart(request):

    return render(request,'axf/main/cart/cart.html')
