from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
    ('S', 'Scan'),
    ('1', 'Phase 1'),
    ('2', 'Phase 2'),
    ('3', 'Phase 3'),
    ('F', 'Final'),
]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    roles=models.CharField(max_length=10,choices=YEAR_IN_SCHOOL_CHOICES,default='Scan')
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile '
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img=Image.open(self.image.path)
        if img.height >300 or img.width >300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
