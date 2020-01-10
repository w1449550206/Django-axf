from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request,'axf/main/cart/cart.html')