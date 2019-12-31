
from django.urls import path, re_path
from booktest import views

urlpatterns = [
    re_path(r'^index$', views.index),  # 首页
    # re_path(r'^shownum(\d+)$', views.shownums),  # 捕获url参数：位置参数
    re_path(r'^shownum(?P<num>\d+)$', views.shownums),  # 捕获url参数：关键字参数，其中?P<ss>中的ss是所选
    # 的捕获参数的名称，需要与视图函数中的参数名称一致
    re_path(r'^login$', views.login),
    re_path(r'login_check', views.lgoin_check),
    re_path(r'text_ajax', views.test_ajax),
    re_path(r'ajax_handle', views.ajax_handle),
    re_path(r'^login_ajax$', views.login_ajax),
    re_path(r'^login_ajax_check$', views.login_ajax_check),
    re_path(r'set_cookie', views.set_cookie),
    re_path(r'get_cookie', views.get_cookie),
    re_path(r'set_session', views.set_session),
    re_path(r'get_session', views.get_session),
    re_path(r'clear_session', views.clear_session),
    re_path(r'change_pwd', views.change_pwd),
    re_path(r'change_pwd_action', views.change_pwd_action)
]
