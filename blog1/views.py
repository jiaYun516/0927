from django.shortcuts import render
from blog1.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    posts=Post.objects.all() #select *
    now=datetime.now()
    return render(request,'index.html',locals())

def showpost(requst,slug):
    try:
        post=Post.objects.get(slug=slug)
        if post!=None: 
            return render(requst,'post.html',locals()) #html跳轉
        else:
            return redirect("/")
    except:
        return redirect("/")  #網址跳轉
    