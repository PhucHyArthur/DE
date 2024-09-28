from django.contrib import admin
from django.urls import include, path


handler404 = 'polls.views.custom_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),  # Include các URL của polls
]
