from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from .models import Oneday_user

# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)     # username : register의 name 항목
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            oneday_user = Oneday_user(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )

            oneday_user.save()

        return render(request, 'register.html', res_data)