from django.shortcuts import render
from .models import Marmot

from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse ('<h1>Hello [\OmO/]</h1>')

def about(request):
    return render(request, 'about.html')

def marmots_index(request):
    return render(request, 'marmots/index.html', { 'marmots': marmots })
