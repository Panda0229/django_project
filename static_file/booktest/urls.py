from django.urls import path, re_path
from booktest import views

urlpatterns = [
    re_path(r'static_test', views.static_test),
    re_path(r'index', views.index),
    re_path(r'show_upload', views.show_upload),
    re_path(r'upload_handle', views.upload_handle),
    re_path(r'show_area(?P<pindex>\d*)', views.show_area),
    re_path(r'areas', views.areas),
    re_path(r'prov', views.prov),
    re_path(r'city(\d+)', views.city),
    re_path(r'^dis(\d+)$', views.dis),
]
