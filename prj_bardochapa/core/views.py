import os
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show_path(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CORE_PATH =  os.path.join( BASE_DIR, 'core', )

    return HttpResponse(os.path.join( CORE_PATH, 'static', ).replace('\\', '/'))

def homepage(request):
    return render(request, 'home.html')