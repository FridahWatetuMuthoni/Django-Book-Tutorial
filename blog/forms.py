from .models import Post
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','slug', 'tags']

class PostDeleteForm(ModelForm):
    class Meta:
        model = Post
        fields = []