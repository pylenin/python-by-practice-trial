from django.shortcuts import render

from .models import Blogs
from newsletter.models import Signup

def index(request):
    course_blogs = Blogs.objects.filter(is_course=True)
    latest_blogs = Blogs.objects.order_by('-timestamp')[0:3]

    if request.method == 'POST':
        email=request.POST['email']
        new_signup = Signup()
        new_signup.email=email
        new_signup.save()
        print(email)

    context = {"object_list":course_blogs,
               "latest_blogs": latest_blogs}
    return render(request, "index.html", context)

def blogs(request):
    return render(request, "blog.html", {})
