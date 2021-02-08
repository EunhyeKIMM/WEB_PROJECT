from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password # 비밀번호 암호화 / 패스워드 체크
from .models import User
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
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
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
        return render(request, 'register.html', res_data)   # register를 요청받으면 register.html로 응답


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