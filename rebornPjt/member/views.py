from django.shortcuts import render, redirect
from django.http import HttpResponse


# 로그인 페이지
def login(request):
    if request.method == 'POST':
        # 입력된 데이터값을
        user_id = request.POST.get('id')
        user_pw = request.POST.get('pw')
        # 콘솔창에 띄운다.
        print(f"아이디 : {user_id}")
        print(f"비밀번호 : {user_pw}")
        
        
        
        return redirect('/')
    else:
        return render(request,'member/login.html')
    







# 회원가입 페이지
def join(request):
    return render(request,'member/join.html')
