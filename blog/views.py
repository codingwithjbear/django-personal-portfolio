from django.shortcuts import render, get_object_or_404 # get_Obj... tries to get and show an object or shows the 404 error
from .models import Blog

# Create your views here.
def all_blogs(request):
    blog_count =  Blog.objects.count
    blogs = Blog.objects.order_by('-date')[:5] 
    #order by -date makes it so the most current posts show first
    # [:5] limits the length to the first 5 blog posts
    # you can add a button to go to the next page to see more post or show more
  ##  blogs = Blog.objects.order_by('-date') 
    return render(request, 'blog/all_blogs.html', {'blogs':blogs,'blogcount':blog_count})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) #pk = primary key for us that is 'id'
    return render(request, 'blog/detail.html',{'blog':blog})