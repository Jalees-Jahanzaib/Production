from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse
from users.models import Profile

# Create your models here.
class Files(models.Model):
   
    title=models.CharField(max_length=100)
    summary=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('file-detail', kwargs={ 'pk' : self.pk} )

class Comment(models.Model):
    files = models.ForeignKey('blog.Files', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    role = models.CharField(max_length=200,default="Scan")
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    stage1=models.CharField(max_length=7,default="False")
    stage2=models.CharField(max_length=7,default="False")
    stage3=models.CharField(max_length=7,default="False")
    final=models.CharField(max_length=7,default="False")

        
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


