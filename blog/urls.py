from django.urls import path
from . import views
#app_name determines a namespace for URLS in this file
#We can now use blog:detail to reference a blog detail
app_name = 'blog'

urlpatterns = [
    path('create/',views.create_post, name='create'),
    path('edit/<int:pk>/', views.edit_post, name='edit'),
    path('delete/<int:pk>/', views.delete_post, name='delete'),
    path('tags/<slug:tag>/', views.home, name='posts_by_tag'),
    path('<slug:slug>/',views.details,name='detail'),
]