from django.shortcuts import render, redirect  # 导入重定向函数
from booktest.models import BookInfo, AreaInfo
from datetime import date
from django.http import HttpResponseRedirect


# Create your views here.
# request参数必须有，request是一个HttpRequest类型的对象
def index(request):
    """显示图书信息"""
    # 查询出所有的图书信息
    books = BookInfo.objects.all()
    # 使用模板
    return render(request, 'booktest/index.html', {'books': books})


def create(request):
    """新增一本图书"""
    # 创建Bookinfo对象
    b = BookInfo()
    b.btitle = '流行蝴蝶剑'
    b.bpub_date = date(2009, 5, 6)
    # 保存进数据库
    b.save()
    # 返回应答, 让浏览器再访问/index
    # return HttpResponse('OK')
    return HttpResponseRedirect('/index')


def delete(request, bid):
    """删除一本书"""
    # 通过bid获取图书对象
    book = BookInfo.objects.get(id=bid)
    # 删除
    book.delete()
    # 重定向,浏览器访问/index
    return HttpResponseRedirect('/index')


def delete(request, bid):
    """删除一本书"""
    # 通过bid获取图书对象
    book = BookInfo.objects.get(id=bid)
    # 删除
    book.delete()
    # 重定向,浏览器访问/index
    # return HttpResponseRedirect('/index')
    return redirect('/index')


def areas(request):
    """获取广州市的上级地区和下级地区"""
    # 获取广州市的信Bookinfo息
    area = AreaInfo.objects.get(atitle='广州市')
    # 上级地区
    parent = area.aParent
    # 下级地区
    children = area.areainfo_set.all()
    # 使用模板文件
    return render(request, 'booktest/area.html', {'area': area, 'parent': parent, 'childrens': children})