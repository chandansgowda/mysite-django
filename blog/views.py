from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("This is Homepage")

def all_posts(request):
    return HttpResponse("This is All Posts Page")

def show_post(request,slug):
    return HttpResponse(f"This is {slug} post")