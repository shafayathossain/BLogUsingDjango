from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        'form':form
    }
    return render(request, "post_form.html", context)
    #return HttpResponse("<h1>create</h1>")

def post_detail(request, id):
    instance = get_object_or_404(Post, id = id)
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
