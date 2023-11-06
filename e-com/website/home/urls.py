from django.urls import path, re_path, include
from home import views

urlpatterns = [
    re_path(r"^$", views.index, name="home"),
]