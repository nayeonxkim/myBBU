from django.urls import path
from . import views

urlpatterns = [
    path('BBU/', views.bbu_list)
]
