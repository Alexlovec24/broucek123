from django.urls import path
from . import  views

urlpatterns = {
    path("bara/", views.models_list)
}