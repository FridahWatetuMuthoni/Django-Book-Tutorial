from .models import Post
from django.forms import ModelForm
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','slug', 'tags','image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'input-group form-control'}),
            #'tags': forms.Textarea(attrs={'class': ' input-group form-control'}),
            #'image': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PostDeleteForm(ModelForm):
    class Meta:
        model = Post
        fields = []