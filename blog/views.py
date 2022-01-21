from django.http import HttpResponse
from django.shortcuts import render

posts_data = [
    {
        "title": "How to learn Python in Kannada?",
        "content": "Go to my youtube channel and learn python in kannada.Videos are already Uploaded",
        "slug": "how-to-learn-python-kannada"
    },
    {
        "title": "How to learn Python in English?",
        "content": "Go to my youtube channel and learn python in english. Videos will be uploaded soon.",
        "slug": "how-to-learn-python-english"
    },
    {
        "title": "How to post a free ad on pgfy",
        "content": "Pgfy has a free plan where you can post any one ad for free for 20 days. Go to www.pgfy.in for more info",
        "slug": "how-to-post-free-ad-on-pgfy"
    },
]

# Create your views here.

def index(request):
    return render(request, "blog/index.html")

def all_posts(request):
    return render(request, "blog/posts.html", {"posts":posts_data})

def show_post(request,slug):
    identified_post = next(post for post in posts_data if post['slug'] == slug)
    return render(request, "blog/post.html", {"post":identified_post})