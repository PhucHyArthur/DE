from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe
from django.views.decorators.gzip import gzip_page
from django.views.decorators.cache import cache_control, never_cache
from django.views.decorators.vary import vary_on_headers

@require_http_methods(["GET", "POST"])
def my_view(request):
    return HttpResponse("This view accepts only GET or POST requests.")

@require_GET
def get_view(request):
    return HttpResponse("This view only accepts GET requests.")

@require_POST
def post_view(request):
    return HttpResponse("This view only accepts POST requests.")

@require_safe
def safe_view(request):
    return HttpResponse("This view only accepts GET and HEAD requests.")

@gzip_page
def compressed_view(request):
    return HttpResponse("This view is compressed with gzip.")

@cache_control(no_cache=True, must_revalidate=True)
def cached_view(request):
    return HttpResponse("This view controls cache headers.")

@never_cache
def no_cache_view(request):
    return HttpResponse("This view should never be cached.")

@vary_on_headers('User-Agent')
def vary_view(request):
    return HttpResponse("This view varies by User-Agent header.")
