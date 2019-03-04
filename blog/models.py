from django.db import models
from django.utils import timezone

# Model을 상속받은 Post 클래스
class Post(models.Model):
    # ForeignKey : 다른 모델에 대한 링크
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # CharField : 글자 수가 제한된 텍스트를 정의할 때 사용
    title = models.CharField(max_length=200)
    # TextField : 글자 수에 제한이 없는 긴 텍스트를 위한 속성
    text = models.TextField()
    # DateTimeField : 날짜와 시간
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # 객체 호출 시 출력할 내용
    def __str__(self):
        return self.title