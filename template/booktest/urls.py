from django.urls import path, re_path
from booktest import views

urlpatterns = [
    re_path(r'^index$', views.index, name='index'),
    re_path(r'^index2$', views.index2),
    re_path(r'^temp_var', views.temp_var),
    re_path(r'temp_tags', views.temp_tags),
    re_path(r'temp_filter', views.temp_filter),
    re_path(r'temp_inhert', views.temp_inhert),
    re_path(r'html_escape', views.html_escape),
    re_path(r'url_reverse', views.url_reverse),
    re_path(r'show_args/(\d+)/(\d+)', views.show_args, name='show_args'),  # 捕获位置参数
    re_path(r'show_kwargs/(?P<c>\d+)/(?P<d>\d+)', views.show_kwargs, name='show_kwargs'),  # 捕获关键字参数
    re_path(r'test_redirect', views.test_redirect)
]
