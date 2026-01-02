from django.shortcuts import render
from django.core.paginator import Paginator
from magazine.models import Magazine, Magazine_code

def mlist(request):
    
    # 매거진 코드 정보
    qs_code = Magazine_code.objects.all()

    # 매거진 리스트
    qs = Magazine.objects.all().order_by('-mdate')

    page = int(request.GET.get('page',1))
    paginator = Paginator(qs,10)
    qs_list = paginator.get_page(page)
    
    if paginator.count < 5:
        etc = 4 - paginator.count
    else:
        etc = 4 - (paginator.count % 4)
        
    context = {'qs_code':qs_code,'list':qs_list,'page':page,'etc_count':etc}
    return render(request,'magazine/mlist.html',context)


