from django.urls import path, re_path
from booktest import views

urlpatterns = [
    re_path(r'set_session', views.set_session),
    re_path(r'get_session', views.get_session)
]
