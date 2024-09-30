from django.urls import path
from . import views

urlpatterns = [
    path('my-view/', views.my_view, name='my_view'),
    path('get-view/', views.get_view, name='get_view'),
    path('post-view/', views.post_view, name='post_view'),
    path('safe-view/', views.safe_view, name='safe_view'),
    path('compressed-view/', views.compressed_view, name='compressed_view'),
    path('cached-view/', views.cached_view, name='cached_view'),
    path('no-cache-view/', views.no_cache_view, name='no_cache_view'),
    path('vary-view/', views.vary_view, name='vary_view'),
]
