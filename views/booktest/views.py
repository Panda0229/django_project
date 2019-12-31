from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


# Create your views here.
# request就是HttpResponse类型的对象
# request包含浏览器请求的信息
def index(request):
    """首页"""
    return render(request, 'booktest/index.html')


def shownums(request, num):
    return HttpResponse("喵了个咪,%s,哈哈" % num)


def login(request):
    """显示登录页面"""
    # 判断用户是否登录
    if request.session.has_key('islogin'):
        # 用户已经登录，跳转到首页
        return redirect('/change_pwd')
    else:
        # 获取cookie username
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'booktest/login.html', {'username': username})


def lgoin_check(request):
    """登录检验视图"""
    # request.POST保存的是post方式提交的参数，是一个QueryDict类型的参数
    # QueryDict是一个类似字典的数据类型，但是可以有相同的键
    # requestGET保存的是get方式提交的参数
    # 1 获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')

    # 2 进行登录的校验
    # 实际开发中根据用户名和密码查找数据可
    if username == 'panda' and password == '123456':
        # 用户名密码正确，跳转到首页,redirct得到的是一个HttpResponseRedict的对象，是HttpResponse的子类，可以创建cookie
        response = redirect('/change_pwd')
        # 判断是否要记住用户名
        if remember == 'on':
            response.set_cookie('username', username, max_age=7*24*3600)
        # 记录用户的登录状态
        # 只要session中有islogin，就认为用户已经登录
        request.session['islogin'] = True
        return response

    else:
        return redirect('/login')


def change_pwd(request):
    return render(request, 'booktest/change_pwd.html')


def change_pwd_action(request):
    """模拟修改密码处理"""
    # 获取新密码
    pwd = request.POST.get('pwd')
    # 实际开发时，修改对应数据库中的内容
    # 返回一个应答
    return HttpResponse('修改密码为：%s' % pwd )


def test_ajax(request):
    """显示ajax界面"""
    return render(request, 'booktest/text_ajax.html')


# 所有的ajax请求都在后台进行
def ajax_handle(request):
    """处理json数据"""
    # 返回json数据{'res':1}
    return JsonResponse({'res': 1})


# /login_ajax
def login_ajax(request):
    """显示ajax登录界面"""
    return render(request, 'booktest/login_ajax.html')


# /login_ajax_check
def login_ajax_check(request):
    """ajax登录校验"""
    # 获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 进行校验
    if username == 'panda' and password == '123456':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})


# /set_cookie
# cookie保存在浏览器端,cookie无论保存的是什么数据类型，取出来的都是字符串
def set_cookie(request):
    """设置一个cookie信息"""
    # 创建cookie必须满足是HttpResponse或其子类的对象
    response = HttpResponse('设置cookie')
    # 设置一个cookie信息,名字为num，值为1,设置存活3600秒，否则浏览器关闭cookie消失
    response.set_cookie('num', 1, max_age=3600)
    # 返回response
    return response


# get_cookie
def get_cookie(request):
    """获取cookie信息"""
    # 取出cookie中num的值
    num = request.COOKIES['num']
    return HttpResponse(num)


# /set_session
# session保存在服务器端，session保存的是什么数据类型，取出来是就是什么数据类型
def set_session(request):
    """设置session"""
    request.session['username'] = 'panda'
    request.session['age'] = 18
    # 如果value是一个整数，会话将在value秒没有活动后过期。
    # 如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期。
    # 如果value为None，那么会话永不过期。
    request.session.set_expiry(10)
    return HttpResponse('设置session')


# /get_session
def get_session(request):
    """取出session"""
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username + ':' + str(age))


# /clear_session
def clear_session(request):
    """清除session"""
    request.session.clear()
    return HttpResponse('清除完毕')
