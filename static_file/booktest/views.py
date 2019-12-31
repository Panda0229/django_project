from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from booktest.models import PicTest, AreaInfo
from django.core.paginator import Paginator


EXCLUDE_IP = ['127.0.0.1']


# 定义阻止访问ip的装饰器
def blocked_ips(view_func):
    def wrapper(request, *args, **kwargs):
        # 获取浏览器端的ip
        user_ip = request.META.get('REMOTE_ADDR')
        print(user_ip)
        if user_ip in EXCLUDE_IP:
            return HttpResponse('<h1>Forbidden</h1>')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


# @blocked_ips
# /static_test
def static_test(request):
    """静态文件"""
    return render(request, 'booktest/static_test.html')


# @blocked_ips
def index(request):
    """首页"""
    print('----index----')
    return render(request, 'booktest/index.html')


# /show_upload
def show_upload(request):
    """显示上传图片页面"""
    return render(request, 'booktest/upload_pic.html')


def upload_handle(request):
    """上传图片处理"""
    # 1 获取上传的图片
    pic = request.FILES.get('pic')
    # 在django中，上传文件不大于2.5M, 文件放在内存中。上传文件大于2.5M, 文件内容写到一个临时文件中。
    # Django处理上传文件的两个类：
    # FILE_UPLOAD_HANDLERS = ("django.core.files.uploadhandler.MemoryFileUploadHandler",
    #                         "django.core.files.uploadhandler.TemporaryFileUploadHandler")

    print(type(pic))
    # 2 创建一个文件                     上传文件保存路径       图片名
    save_path = '%s/booktest/%s' % (settings.MEDIA_ROOT, pic.name)
    with open(save_path, 'wb') as f:
        # 文件通过pic.chunks传文件
        for content in pic.chunks():
            f.write(content)

    # 3 在数据库中保存上传记录
    PicTest.objects.create(goods_pic='booktest/%s' % pic.name)

    # 4 返回
    return HttpResponse('OK')


# /show_area页码
# 前段访问时需要传递页码
def show_area(request, pindex):
    """分页"""
    # 1 查询出多有省级地区的信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)

    # 2 分页 , 每页显示10条
    paginator = Paginator(areas, 10)
    # 返回总页数
    # print(paginator.num_pages)
    # 返回页数列表
    # print(paginator.page_range)

    # 3 获取pindex页的内容, page是Page类的实例对象
    if pindex == '':
        # 默认取第一页内容
        pindex = 1
    else:
        pindex = int(pindex)
    page = paginator.page(int(pindex))
    # # 打印当前页的页码
    # print(page.number)

    # 4 使用模板
    return render(request, 'booktest/show_area.html', {'page': page})


# /areas
def areas(request):
    """省市县"""
    return render(request, 'booktest/areas.html')


# /prov
def prov(request):
    """过去获取所有省级地区信息"""
    # 1 获取所有省级地区的信息
    # 查询集不可以直接放到json数据中，需要自己进行拼接
    areas = AreaInfo.objects.filter(aParent__isnull=True)

    # 2 遍历areas，并拼接处json数据:atitle id
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))

    # 2 返回数据
    return JsonResponse({'data': areas_list})


# /city
def city(request, pid):
    """获取省级地区以下的市级地区"""
    # 1 获取pid对应的省级地区
    # area = AreaInfo.objects.get(id=pid)
    # areas = area.areainfo_set.all()
    areas = AreaInfo.objects.filter(aParent__id=pid)

    # 2 遍历areas，并拼接处json数据:atitle id
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))

    # 2 返回数据
    return JsonResponse({'data': areas_list})


def dis(request, pid):
    '''获取pid的下级地区的信息'''
    # 1.获取pid对应地区的下级地区
    # area = AreaInfo.objects.get(id=pid)
    # areas = area.areainfo_set.all()
    areas = AreaInfo.objects.filter(aParent__id=pid)

    # 2.变量areas并拼接出json数据：atitle id
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))

    # 3.返回数据
    return JsonResponse({'data': areas_list})













