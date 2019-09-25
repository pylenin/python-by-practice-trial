from django.shortcuts import render

from .models import Blogs
def index(request):
    course_blogs = Blogs.objects.filter(is_course=True)
    latest_blogs = Blogs.objects.order_by('-timestamp')[0:3]

    context = {"object_list":course_blogs,
               "latest_blogs": latest_blogs}
    return render(request, "index.html", context)

def blogs(request):
    return render(request, "blog.html", {})
