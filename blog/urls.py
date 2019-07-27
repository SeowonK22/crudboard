from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('<int:blog_id>/', blog.views.detail, name='detail'), # 각 게시물의 id값을 받아 url 디자인
    path('new/', blog.views.new, name='new'),
    path('<int:blog_id>/edit/', blog.views.edit, name='edit'),
    path('<int:blog_id>/delete/', blog.views.delete, name='delete'),
]