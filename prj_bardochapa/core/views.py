import os
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show_path(request):
    path = os.path.join( os.path.dirname(__file__), 'static',  )
    return render(request, 'base.html')