from django.shortcuts import render
from blog1.models import Post
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def homepage(request):
    posts=Post.objects.all() #select *
    now=datetime.now()
    return render(request,'index.html',locals())

def showpost(requst,slug):
    post=Post.objects.get(slug=slug)
    return render(requst,'show.html',locals())
    