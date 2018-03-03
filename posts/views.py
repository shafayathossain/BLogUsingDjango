from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
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
    paginator = Paginator(queryset, 1)
    page = request.GET.get('page')
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        query_set = paginator.page(1)
    except EmptyPage:
        query_set = paginator.page(paginator.num_pages)
    context = {
        'title':'list',
        'object_list':query_set
        }
    return render(request, "post_list.html", context)
def post_update(request, id):
    instance = get_object_or_404(Post, id = id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form':form
    }
    return render(request, "post_form.html", context)
def post_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect("posts:list")
def post_home():
    return HttpResponse("<h1>hello</h1>")
