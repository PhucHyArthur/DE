from django.shortcuts import render

def index(request):
    context = {'name': 'Thế giới'}
    return render(request, 'myapp/index.html', context)
