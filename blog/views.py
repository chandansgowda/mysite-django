from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "blog/index.html")

def all_posts(request):
    return render(request, "blog/posts.html", {"posts":posts_data})

def show_post(request,slug):
    identified_post = next(post for post in posts_data if post['slug'] == slug)
    return render(request, "blog/post.html", {"post":identified_post})