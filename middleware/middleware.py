from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginMiddle(MiddlewareMixin):

    def process_request(self,request):

        LOGIN_HTML_REQUEST=[
            '/axfcart/cart/',
            '/axfmine/mine/'
        ]


        LOGIN_JSON_REQUEST = [
            '/axfcart/addToCart/'
        ]



        if request.path in LOGIN_HTML_REQUEST:
            user_id = request.session.get('user_id')

            if user_id:
                # 自定义属性   给request对象自己设定一个属性值
                # 然后可以通过request.user_id获取
                request.user_id = user_id
            else:
                return redirect(reverse('axfuser:login'))

        if request.path in LOGIN_JSON_REQUEST:
            user_id = request.session.get('user_id')

            if user_id:
                request.user_id = user_id

            else:
                data = {
                    'status':201
                }

                return JsonResponse(data=data)

