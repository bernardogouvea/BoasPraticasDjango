from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        return render(request, 'galeria/index.html')
        #return HttpResponse('<h1>Bernartozóide2</h1>')