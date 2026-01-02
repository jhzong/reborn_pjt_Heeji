from django.db import models  # 장고에서 데이터베이스 도구(models)를 불러옵니다.

# Post라는 이름의 테이블(표)을 정의합니다.
# models.Model을 상속받아야 장고가 "이건 데이터베이스용 클래스구나!"라고 인식합니다.
class Post(models.Model):
    # 제목: 최대 200자까지 저장할 수 있는 문자열 칸을 만듭니다. (글자 수 제한 있음)
    title = models.CharField(max_length=200)

    # 내용: 글자 수 제한이 없는 긴 텍스트를 저장하는 칸을 만듭니다.
    content = models.TextField()

    # 작성자: 최대 50자 문자열 칸. 글을 쓸 때 이름을 안 적으면 기본값으로 '익명'이 들어갑니다.
    author = models.CharField(max_length=50, default='익명')

    # 작성일: 날짜와 시간을 저장합니다. 
    # auto_now_add=True는 "글이 처음 저장되는 순간의 시간"을 자동으로 기록하라는 뜻입니다.
    created_at = models.DateTimeField(auto_now_add=True)

    # 조회수: 0 이상의 양수만 저장하는 숫자 칸입니다. 
    # default=0은 처음 글이 올라오면 조회수가 0부터 시작한다는 뜻입니다.
    views = models.PositiveIntegerField(default=0)

    # 이 함수는 관리자 페이지(Admin)나 터미널에서 데이터를 조회할 때,
    # 글 번호(Post object) 대신 실제 '글 제목'이 보이게 해주는 역할을 합니다.
    def __str__(self):
        return self.title