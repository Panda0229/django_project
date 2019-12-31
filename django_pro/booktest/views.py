from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo, HeroInfo
from django.template import loader


# Create your views here.
# def my_rende(request, template, context={}):
#     # 使用模板文件
#     # 1 加载模板文件,返回模板对象
#     temp = loader.get_template(template)
#
#     # 2 定义模板上下文，给模板文件传数据
#     context = context
#
#     # 3 模板渲染，产生标准的html内容
#     res_html = temp.render(context)
#
#     # 4 返回给浏览器
#     return HttpResponse(res_html)


# 1 定义视图函数
# 2 进行url配置，建立url地址和视图的对应关系
# http://127.0.0.1:8000/index
def index(request):
    # 进行处理，和M和T进行交互
    # return HttpResponse('喵了个咪')
    # return my_rende(request, 'booktest/index.html')
    return render(request, 'booktest/index.html', {'content': 'hello word'})


def index2(request):
    return HttpResponse('哗啦哗啦')


def showbooks(request):
    """显示视图的信息"""
    # 1 通过M查找图书表中的数据
    book = BookInfo.objects.all()
    # 2 使用模板
    return render(request, 'booktest/showbooks.html',
                  {'books': book})


def detail(request, bid):
    """查询图书关联人物信息"""
    # 1 根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)
    # 2 查询和book关联的人物信息
    heros = book.heroinfo_set.all()
    # 3 使用模板
    return render(request, 'booktest/detail.html', {'book': book, 'heros':heros})
