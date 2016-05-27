from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def post_create(request):
    return HttpResponse("<h1> create</h1>")


def post_detail(request):
    context = {
        "title": "List"
    }
    return render(request, "index.html", context)
    #return HttpResponse("<h1> detail</h1>")


def post_list(request):
    context = {
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