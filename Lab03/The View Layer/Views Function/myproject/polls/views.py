from django.http import HttpResponse
import datetime
from django.http import Http404
from django.core.exceptions import PermissionDenied

def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now}.</body></html>"
    return HttpResponse(html)

def custom_404_view(request, exception):
    raise Http404("Page not found!")

def custom_permission_denied_view(request, exception):
    raise PermissionDenied

async def async_current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now}.</body></html>"
    return HttpResponse(html)