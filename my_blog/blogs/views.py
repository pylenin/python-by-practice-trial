from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q

from .models import Blogs
from newsletter.models import Signup

def search_results(request):
    blog_list = Blogs.objects.all()
    query = request.GET.get("q")

    if query:
        blog_list=blog_list.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()

    context = {
        "queryset":blog_list,
    }
    return render(request, "search_results.html", context)

def get_category_count():
    blog_categories = Blogs.objects.values('categories__title').annotate(Count('categories'))
    return blog_categories

def index(request):
    course_blogs = Blogs.objects.filter(is_course=True)
    latest_blogs = Blogs.objects.order_by('-timestamp')[0:3]

    if request.method == 'POST':
        email=request.POST['email']
        new_signup = Signup()
        new_signup.email=email
        new_signup.save()

    context = {"object_list":course_blogs,
               "latest_blogs": latest_blogs}
    return render(request, "index.html", context)

def blogs(request):
    category_count = get_category_count()
    blog_list = Blogs.objects.order_by('-timestamp')
    paginator = Paginator(blog_list, 4)
    page_request_variable = 'page'
    page = request.GET.get(page_request_variable)

    try:
        paginator_query_set = paginator.page(page)
    except PageNotAnInteger:
        paginator_query_set = paginator.page(1)
    except EmptyPage:
        paginator_query_set = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        email=request.POST['email']
        new_signup = Signup()
        new_signup.email=email
        new_signup.save()

    context = {
        "blog_list":paginator_query_set,
        "page_request_variable":page_request_variable,
        "category_count":category_count
    }
    return render(request, "blog.html", context)

def posts(request, slug):
    return render(request, "post.html", {})
