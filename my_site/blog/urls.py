from django.urls import path
#import dulu view kita yang di app dengan code berikut "." itu menandakan semua yang ada di folder ini bisa di detect
from . import views
urlpatterns = [
    path("", views.starting_page, name= "starting-page"), 
    path("posts", views.posts, name = "posts-page"),
    path("posts/<slug:slug>", views.post_detail, name = "post-detail-page")
]
