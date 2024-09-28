from django.urls import path
from . import views

handler403 = 'polls.views.custom_permission_denied_view'
urlpatterns = [
    path('time/', views.current_datetime, name='current_datetime'),
    path('async_time/', views.async_current_datetime, name='async_current_datetime'),
]

