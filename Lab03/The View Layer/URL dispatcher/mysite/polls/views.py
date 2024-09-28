from django.http import HttpResponse
from django.views.generic import View

class IndexView(View):
    def get(self, request):
        return HttpResponse("Welcome to the polls index!")

class DetailView(View):
    def get(self, request, pk):
        return HttpResponse(f"Poll detail for ID {pk}")
