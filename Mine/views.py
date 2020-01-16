from django.shortcuts import render

# Create your views here.
from User.models import AxfUser


def mine(request):

    # user_id = request.session.get('user_id')

    user_id = request.user_id

    if user_id:

        user = AxfUser.objects.get(pk=user_id)

        context = {
            'user':user
        }

        return render(request,'axf/main/mine/mine.html',context=context)
    else:
        return render(request, 'axf/main/mine/mine.html')