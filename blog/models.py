from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    #image = models.ImageField(upload_to='featured_image/%Y/%m/%d/')
    #name = models.CharField(max_length=10)
    #photo = models.ImageField(upload_to="%Y/%m/%d")
    

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title 

# 
class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

# 마이그레이트 이미지싱크: --run-syncdb은 마이그레이션을 하지않고 테이블을 만든다는 뜻이라고 함. 무슨말인지는 모르겠음 
  #  python manange.py migrate --run-syncdb 