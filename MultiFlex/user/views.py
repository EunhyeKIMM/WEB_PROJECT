from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password # 비밀번호 암호화 / 패스워드 체크
from .models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
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
<<<<<<< HEAD
            return redirect('register_done.html')
            # return render(request, 'register_done.html', res_data)   # register를 요청받으면 register.html로 응답
            

@login_required # 로그인 된 상태에서만 사용 가능
def userpage(request):
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

# def userinfo(request):  # 유저 마이페이지
#     connect_user = request.user

#     context = {
#         'email' : connect_user.email,
#         'username' : connect_user.username,
#         'phone' : connect_user.phone,
#         'gender' : connect_user.gender,
#         'age' : connect_user.age
#     }
#     return render(request, 'mypage_info.html', context=context)
    

# class UserDV(DetailView):
#     model = User
#     context_object_name = 'mypage'
#     template_name = 'user/mypage.html'
   
#     # Detail View에서는 paginate_by없기 때문에 만들어줘야 한다
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         video = context['video']
#         review_list = video.review_set.all()   #.order_by('-create_dt')[:5]
#         paginator = Paginator(review_list, 2) #한 페이지에 보여줄 개수 
        
#         page_number = self.request.GET.get('page') # 현재 페이지 받아옴
#         page_obj = paginator.get_page(page_number) # 현재 페이지에 있는 목록 

#         context['paginator'] = paginator
#         context['page_obj'] = page_obj #페이지 목록
#         return context

=======
            return render(request, 'register_done.html', res_data)   # register를 요청받으면 register.html로 응답
>>>>>>> master


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