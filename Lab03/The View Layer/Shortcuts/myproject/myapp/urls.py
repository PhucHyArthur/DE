# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('my-view/', views.my_view, name='my_view'),
    path('redirect/', views.redirect_view, name='redirect_view'),
]
