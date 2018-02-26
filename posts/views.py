from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.
def post_create(request):
    return render(request, "index.html", {})
    #return HttpResponse("<h1>create</h1>")
def post_detail(request):
    instance = get_object_or_404(Post, id = 1)
    context = {
        'title':'detail',
        'obj':instance
    }
    return render(request, "post_detail.html", context)
def post_list(request):
    queryset = Post.objects.all()
    context = {
        'title':'list',
        'object_list':queryset
        }
    return render(request, "index.html", context)
def post_update(request):
    return HttpResponse("<h1>update</h1>")
def post_delete(request):
    return HttpResponse("<h1>delete</h1>")
def post_home():
    return HttpResponse("<h1>hello</h1>")
