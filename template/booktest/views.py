from django.shortcuts import render, redirect, HttpResponse
from booktest.models import BookInfo
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'booktest/index.html')


# 1)	首先去配置的模板目录下面去找模板文件。
# 2)	去INSTALLED_APPS下面的每个应用的templates去找模板文件，前提是应用中必须有templates文件夹。
def index2(request):
    return render(request, 'booktest/index2.html')


# /temp_var
def temp_var(request):
    '''模板变量'''
    my_dict = {'title': '字典键值'}
    my_list = [1, 2, 3]
    book = BookInfo.objects.get(id=1)

    context = {'my_dict': my_dict, 'my_list': my_list, 'book': book}
    return render(request, 'booktest/temp_var.html', context)


# /temp_tags
def temp_tags(request):
    """模板标签"""
    books = BookInfo.objects.all()
    return render(request, 'booktest/temp_tags.html', {'books': books})


# /temp_filter
def temp_filter(request):
    """模板过滤器"""
    books = BookInfo.objects.all()
    return render(request, 'booktest/temp_filter.html', {'books': books})


# /temp_inhert
def temp_inhert(request):
    """模板继承"""
    return render(request, 'booktest/child.html')


# /html_escape
def html_escape(request):
    """模板转义"""
    return render(request, 'booktest/html_escape.html', {'content': '<h1>hello<h1>', 'detail': '<h1>goodby<h1>'})


def url_reverse(request):
    """url反向解析"""
    return render(request, 'booktest/url_reverse.html')


def show_args(request, a, b):
    return HttpResponse(a+';'+b)


def show_kwargs(request, c, d):
    return HttpResponse(c+';'+d)


def test_redirect(request):
    """重定向到首页"""
    # return render('/index')
    # url = reverse('booktest:index')
    # return redirect(url)

    # 重定向到/show_args/1/2
    url = reverse('booktest:show_args', args=(1, 2))
    return redirect(url)


















