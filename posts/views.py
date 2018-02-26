from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_create(request):
    return render(request, "index.html", {})
    #return HttpResponse("<h1>create</h1>")
def post_detail(request):
    context = {'title':'detail'}
    return render(request, "index.html", context)
def post_list(request):
    if request.user.is_authenticated():
        context = {'title':'user list'}
    else:
        context = {'title':'list'}
    return render(request, "index.html", context)
def post_update(request):
    return HttpResponse("<h1>update</h1>")
def post_delete(request):
    return HttpResponse("<h1>delete</h1>")
def post_home():
    return HttpResponse("<h1>hello</h1>")
