from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the blog index!")

def archive(request):
    return HttpResponse("Welcome to the blog archive!")
