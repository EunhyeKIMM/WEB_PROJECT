# from typing import List
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password # 비밀번호 암호화
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import User
from .form import CheckPasswordForm

# Create your views here.

def register(request):  # 회원가입 함수
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        email = request.POST.get('email') # 사전형태
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        res_data = {}                       # 위 html 파일에서 {{erorr}}와 맵핑되어 처리
        
        if not (email and password and re_password and age and gender and phone and username) :
            res_data['error'] = "모든 값을 입력해야 합니다."
            return render(request, 'register.html', res_data)
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
            return render(request, 'register.html', res_data)
        else :
            user = User(
                email = email, 
                password = make_password(password), 
                age = age,
                gender = gender,
                phone = phone,
                username = username
            )
            user.save()
            return HttpResponseRedirect(reverse('register_done'))
            
@login_required # 로그인 된 상태에서만 사용 가능
def userPage(request):  # 유저 마이페이지
    connect_user = request.user

    context = {
        'username' : connect_user.username,
        'email' : connect_user.email,
        'username' : connect_user.username,
        'phone' : connect_user.phone,
        'gender' : connect_user.gender,
        'age' : connect_user.age
    }
    return render(request, 'mypage.html', context=context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다!')
            return redirect('/')
        else:
            messages.error(request, '비밀번호가 맞지 않습니다.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def delete(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)
        
        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('/accounts/login/')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'user_delete.html', {'password_form':password_form})

@login_required
def update(request):
    if request.method == 'GET':
        return render(request, 'user_update.html')

    elif request.method == 'POST':
        user=request.user

        username = request.POST.get('username')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        phone = request.POST.get('phone')

        user.username = username
        user.gender = gender
        user.age = age
        user.phone = phone
        user.save()
        return redirect('/user/')
        

# def login(request):
#     response_data = {}
#     print('------------------', request.method)

#     if request.method == "GET" :
#         return render(request, 'login.html')

#     elif request.method == "POST":
#         login_email = request.POST.get('email', None)
#         login_password = request.POST.get('password', None)

#         if not (login_email and login_password):
#             response_data['error'] = "이메일과 비밀번호를 모두 입력해주세요."
#         else:
#             user = User.objects.get(email=login_email)
#             # db에서 꺼내는 명령. POST로 받아온 email 으로, DB의 email을 꺼내온다.
#             if check_password(login_password, user.password):
#                 request.session['user'] = user
#                 # 세션도 딕셔너리 변수 사용과 똑같이 사용하면 됨.
#                 # 세션 user라는 key에 방금 로그인한 email을 저장.
#                 return redirect('/')
#             else:
#                 response_data['error'] = "비밀번호를 틀렸습니다."
        
#         return render(request, 'login.html', response_data)

# def logout(request):
#     request.session.pop('user')
#     return redirect('/')

# def home(request):
#     email = request.session.get('user')
#     if email:
#         user_info = User.objects.get(pk=email)  # 세션에 넣어놨던 email값을 pk로 하여 데이터를 꺼내옴.
#         return HttpResponse(user_info.email)    # 로그인을 했으면 email을 출력

#     return HttpResponse("로그인을 해주세요")     # 세션에 user가 없으면 뜸 (로그인 안했을때)