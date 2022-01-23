from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

# Create your views here.

def index(request):
    return render(request, "blog/index.html")

def all_posts(request):
    posts = Post.objects.all()
    return render(request, "blog/posts.html", {"posts":posts})

def show_post(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post.html", {"post":post})