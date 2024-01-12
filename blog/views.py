from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, PostDeleteForm
from django.contrib.auth.decorators import permission_required
from taggit.models import Tag
from django.core.paginator import Paginator


# Create your views here.
def home(request, tag=None):
    tag_obj = None
    if not tag:
        posts = Post.objects.all()
    else:
        tag_obj = get_object_or_404(Tag, slug=tag)
        posts = Post.objects.filter(tags__in=[tag_obj])
    
    #pagination
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    content = {
        'posts':posts,
        'section':'home',
        'tag':tag_obj
    }
    return render(request, 'home.html',content)

def details(request, slug=None):
    post  = get_object_or_404(Post, slug=slug)
    
    content = {
        'section':'blog_detail',
        'post':post
    }
    return render(request, "blog/detail.html",content)

@permission_required('blog.add_post', raise_exception=True)
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        content = {
            'section':'blog_create',
            'form':form
        }
    return render(request, 'blog/create.html',content)

@permission_required('blog.change_post',raise_exception=True)
def edit_post(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:detail',slug=post.slug)
    else:
        form = PostForm(instance=post)
    content = {
        'form':form,
        'section':'blog_edit',
        'post':post
    }
    return render(request,'blog/update.html',content)

@permission_required('blog.delete_post',raise_exception=True)
def delete_post(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostDeleteForm(request.POST, instance=post)
        if form.is_valid():
            post.delete()
            return redirect('home')
    else:
        form = PostDeleteForm(instance=post)
    
    content = {
        'section':'blog_delete',
        'form':form,
        'post':post
    }
    return render(request, 'blog/delete.html', content)
