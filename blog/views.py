from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import New

# Create your views here.
    
def home(request):
    blogs = Blog.objects
    blog_list=Blog.objects.all()
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'home.html',{'blogs':blogs,'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'POST':
        form = New(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date=timezone.datetime.now()
            blog.save()
            return redirect('home')
    else:
        form = New(instance=blog)
        return render(request,'edit.html', {'form':form})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('home')


def new(request):
    if request.method =='POST':
        form = New(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.datetime.now()
            post.save()
            return redirect('home')
    else:
        form = New()
        return render(request,'new.html', {'form':form})

