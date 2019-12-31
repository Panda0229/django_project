from django.urls import path, re_path
from booktest import views


# 在应用的urls中进行url配置的时候
# 1 严格匹配开头和结尾
urlpatterns = [
    # 通过url函数设置url路由配置
    path('index', views.index),  # 建立/index和视图index之间的关系
    path('index2', views.index2),
    path('books', views.showbooks),  # 显示图书信息
    re_path(r'books/(\d+)$', views.detail),  # 显示英雄信息
]