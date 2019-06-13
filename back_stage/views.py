from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

# -------str-------
from django.http import HttpResponse 

# 首界面
def index(request):
    # return HttpResponse('Hello World!')
    return render(request, 'blank_page.html',{})


def blog_list(request):
    return render(request, 'blog-list.html',{})
