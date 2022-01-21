from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="homepage"),
    path("posts/",views.all_posts, name="all-posts-page"),
    path("posts/<str:slug>", views.show_post, name="single-post-page")
]