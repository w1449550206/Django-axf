import uuid
from io import BytesIO

from PIL import Image
from PIL.ImageDraw import ImageDraw
from PIL import ImageFont





from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse

from User.models import AxfUser
from User.view_constaint import send_email
from axf import settings


def login(request):
    if request.method == 'GET':
        return render(request,'axf/user/login.html')
    elif request.method == 'POST':
#         先判断验证码是否正确    生成的验证码 和 文本框中的验证码
#         然后判断用户名子和密码
        imgcode = request.POST.get('imgcode')

        imgcode1 = request.session.get('verify_code')

        if imgcode.lower() == imgcode1.lower():

            name = request.POST.get('name')

            users = AxfUser.objects.filter(name=name)

            if users.exists():

                user = users.first()

                password = request.POST.get('password')


                b = check_password(password,user.password)

                if b:
                    if user.active:
                        # session是不可以绑定对象
                        request.session['user_id']=user.id

                        return redirect(reverse('axfmine:mine'))
                    else:
                        context = {
                            'msg': '帐号未激活'
                        }

                        return render(request, 'axf/user/login.html', context=context)
                else:
                    context = {
                        'msg': '密码错误'
                    }

                    return render(request, 'axf/user/login.html', context=context)
            else:
                context = {
                    'msg': '用户名字错误'
                }
                return render(request, 'axf/user/login.html', context=context)



        else:

            context = {
                'msg':'验证码错误'
            }

            return render(request,'axf/user/login.html',context=context)




def register(request):
    if request.method == 'GET':
        return render(request,'axf/user/register.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')


        # make_password会将字符串进行加密 每次加密的结果都是不一样的
        # check_password的语法是（原字符串，加密后的字符串）
        password = make_password(password)


        user = AxfUser()

        user.name = name
        user.password = password
        user.email = email
        user.icon = icon

        token = uuid.uuid4()

        user.token = token

        user.save()

        cache.set(token,user.id,timeout=60)

        send_email(name,email,token)

        return redirect(reverse('axfuser:login'))


def checkName(request):
    # ajax发送的请求的返回值 必须是json

    name = request.GET.get('name')

    users = AxfUser.objects.filter(name=name)

    data = {
        'msg': '用户名字可以使用',
        'status': 200,
    }

    if users.count() > 0:
        data['msg'] = '用户名字已存在'
        data['status'] = 201
        return JsonResponse(data=data)
    else:
        return JsonResponse(data=data)


def testSendMail(request):
    # subject 主题
    # message 内容
    # from_email 发送者
    # recipient_list 接收者

    subject = '爱鲜锋发送邮件'
    message = '<h1>买水果送免费搓澡一次</h1>'

    index = loader.get_template('axf/user/active.html')

    context = {
        'name':'司明宇',
        'url':'http://www.1000phone.com'
    }

    result = index.render(context=context)


    html_message = result
    from_email = 'yulin_ljing@163.com'
    recipient_list = ['yulin_ljing@163.com']

    # 当有html_message的情况下  那么message则不生效
    # message的参数必须书写，但是写上还没有多大作用
    send_mail(subject=subject,message=message,html_message=html_message,from_email=from_email,recipient_list=recipient_list)



    return HttpResponse('<h1>发送邮件成功</h1>')


def account(request):
    # 要激活的是注册的那个帐号
    #   解决方法：传过来一个参数  这个参数必须是当前对象的唯一标识
    #        注意不要使用敏感信息  eg:id name email

    # token的值和cache设置的那个值是一致的
    token = request.GET.get('token')

    user_id = cache.get(token)

    if user_id:

        user = AxfUser.objects.filter(token=token)[0]

        user.active = True

        user.save()
        # 将缓存中的token删除
        cache.delete(token)

        return HttpResponse('激活成功')
    else:
        return HttpResponse('邮件已过期，请重新发送！！！')



def get_code(request):

    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (150, 50)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 50)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(40*i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")



import random


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code


def logout(request):

    request.session.flush()

    return redirect(reverse('axfmine:mine'))