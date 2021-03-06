from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post

def post_create(request):
    return HttpResponse("<h1> create</h1>")


def post_detail(request,id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "object_list": instance,
        "instance": instance,
        "title": instance.title,
    }
    return render(request, "post_detail.html", context)
    #return HttpResponse("<h1> detail</h1>")


def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list":queryset,
        "title": "List"
    }
    return render(request, "index.html", context)
    #eturn HttpResponse("<h1>list</h1>")


def post_update(request):
    context = {
        "title": "List"
    }
    return render(request, "index.html", context)


def post_delete(request):
    return HttpResponse("<h1>delete</h1>")