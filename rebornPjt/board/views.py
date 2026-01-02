from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

def blist(request):
    # 1. 모든 게시글을 가져옵니다. (변수명을 posts로 통일)
    posts = Post.objects.all().order_by('-id') 
    
    # 2. Paginator 설정 (첫 번째 인자에 위에서 선언한 변수 posts를 넣어야 합니다)
    paginator = Paginator(posts, 10) # 10개씩 자르기
    
    # 3. 현재 페이지 번호를 가져오고 해당 페이지 객체를 생성합니다.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # 4. 템플릿으로 데이터를 보냅니다. 
    # (page_obj를 'posts'라는 이름으로 전달하면 HTML의 {% for post in posts %}가 작동합니다)
    return render(request, 'board/blist.html', {'posts': page_obj})


def notice(request):
    # 만약 DB에 '공지사항' 카테고리가 따로 있다면 필터링해서 가져올 수도 있습니다.
    # 지금은 단순히 notice.html을 보여주는 코드로 작성할게요.
    return render(request, 'board/notice.html')




def bwrite(request):
    return render(request,'board/bwrite.html')


