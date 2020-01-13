from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from User.models import AxfUser


def login(request):
    return render(request,'axf/user/login.html')


def register(request):
    if request.method == 'GET':
        return render(request,'axf/user/register.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')


        user = AxfUser()

        user.name = name
        user.password = password
        user.email = email
        user.icon = icon

        user.save()

        return HttpResponse('火红的萨日朗')


def checkName(request):
    # ajax发送的请求的返回值 必须是json

    name = request.GET.get('name')

    users = AxfUser.objects.filter(name=name)

    data = {
        'msg': '用户名字可以使用~',
        'status': 200,
    }

    if users.count() > 0:
        data['msg'] = '用户名字已存在~'
        data['status'] = 201
        return JsonResponse(data=data)
    else:
        return JsonResponse(data=data)
