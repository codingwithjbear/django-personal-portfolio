from django.urls import path, include
from . import views

app_name = 'blog' #declaring the app name will help limit errors if another app has the same page name "detail" in our example

urlpatterns = [
    path('',views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/',views.detail, name='detail'), # if any one enters an integer after blog I want you to represent that integer as the blog id
]