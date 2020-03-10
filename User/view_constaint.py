from django.core.cache import cache
from django.core.mail import send_mail
from django.template import loader


def send_email(name,email,token):
    subject = '爱鲜锋发送邮件'
    message = '<h1>买水果送免费搓澡一次</h1>'

    index = loader.get_template('axf/user/active.html')


    context = {
        'name': name,
        'url': 'http://127.0.0.1:8000/axfuser/account/?token='+str(token)
    }

    result = index.render(context=context)

    html_message = result
    from_email = 'w1449550206@163.com'
    recipient_list = [email]

    # 当有html_message的情况下  那么message则不生效
    # message的参数必须书写，但是写上还没有多大作用
    send_mail(subject=subject, message=message, html_message=html_message, from_email=from_email,
              recipient_list=recipient_list)
