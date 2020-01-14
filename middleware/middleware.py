from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginMiddle(MiddlewareMixin):

    def process_request(self,request):

        LOGIN_HTML_RQQUEST=[
            '/axfcart/cart/'
        ]

        if request.path in LOGIN_HTML_RQQUEST:
            user_id = request.session.get('user_id')

            if not user_id:
                return redirect(reverse('axfuser:login'))

