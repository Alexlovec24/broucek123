from django.urls import path
from . import views

urlpatterns = {
    path("randomnumber/", views.blog_list, name="blog_list")
}