from django.contrib import messages
from django.shortcuts import redirect, render
from member.models import MyUser  # 사용자님이 만든 모델
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password

# 1. 정보 수정 화면 보여주기
def mychange(request):
    # 세션에서 로그인한 아이디('haeon') 가져오기
    user_session_id = request.session.get("user_id")
    
    if not user_session_id:
        return redirect('member:login')

    try:
        # User 대신 MyUser 모델을 직접 사용하여 mem_id 필드로 조회
        user = MyUser.objects.filter(mem_id=user_session_id).first()
        
        if not user:
            messages.error(request, "사용자 정보를 찾을 수 없습니다.")
            return redirect('member:login')

        # DB에서 가져온 user 객체를 템플릿으로 전달
        return render(request, 'mypage/mychange.html', {'user': user})
        
    except Exception as e:
        print(f"Error: {e}")
        return redirect('member:login')

# 2. 정보 수정 데이터 처리
def mychange_update(request):
    if request.method == "POST":
        # 폼에서 넘어온 아이디
        mem_id = request.POST.get('mem_id')
        
        try:
            # 사용자 아이디로 객체 찾기
            user = MyUser.objects.get(mem_id=mem_id)
            
            # 폼 데이터 업데이트
            user.mem_nm = request.POST.get('mem_nm')
            user.nick_nm = request.POST.get('nick_nm')
            user.email = request.POST.get('email')
            user.zip_code = request.POST.get('zip_code')
            user.base_addr = request.POST.get('base_addr')
            user.detail_addr = request.POST.get('detail_addr')
            
            # 비밀번호 변경 처리 (AbstractBaseUser의 set_password 사용)
            new_pw = request.POST.get('mem_pw')
            if new_pw:
                user.mem_pw = make_password(new_pw) 
            
            # DB 저장
            user.save()
            
            logout(request)
            # 세션 정보 삭제 및 로그아웃
            if "user_id" in request.session:
                del request.session["user_id"]
            
            messages.success(request, "정보 수정이 완료되었습니다. 다시 로그인해 주세요.")
            
            # 로그인 페이지로 이동 (URL name이 'member:login'인 경우)
            return redirect('member:login')
            
        except MyUser.DoesNotExist:
            messages.error(request, "수정하려는 사용자 정보를 찾을 수 없습니다.")
            return redirect('mypage:mychange')
        except Exception as e:
            messages.error(request, f"오류가 발생했습니다: {str(e)}")
            return redirect('mypage:mychange')

    # POST가 아닐 경우
    return redirect('mypage:mychange')

# 3. 중복 확인 (MyUser 기준으로 수정)
def check_duplicate(request):
    field = request.GET.get('field')
    value = request.GET.get('value')
    # 현재 세션 유저 아이디 가져오기
    current_user_id = request.session.get("user_id")
    
    # 본인의 현재 값 제외하고 중복 체크
    exists = MyUser.objects.exclude(mem_id=current_user_id).filter(**{field: value}).exists()
    
    return JsonResponse({'exists': exists})

def myaccount(request):
    # 회원탈퇴 페이지나 계정 관리 페이지를 렌더링합니다.
    # 해당 html 파일이 없다면 일단 아래처럼 작성해 두세요.
    return render(request, 'mypage/myaccount.html')