from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length =255)
    body = models.TextField()
    slug = models.SlugField(max_length = 255, blank=True, default='')
    date = models.DateTimeField(auto_now_add = True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.CASCADE)
    image = models.ImageField(default='',blank=True, upload_to='images')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(1200,300)], format = 'JPEG', options={'quality': 60})
    tags = TaggableManager()
    
    def __str__(self):
        return self.title
    
    """
    By overriding the save method, we can execute custom logic before 
    the object is stored in the database.
    """
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:detail', args=[str(self.slug)])