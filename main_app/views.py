from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Marmot

class MarmotCreate(CreateView):
  model = Marmot
  fields = '__all__'

class MarmotUpdate(UpdateView):
  model = Marmot
  fields = ['species', 'description', 'age']

class MarmotDelete(DeleteView):
  model = Marmot
  success_url = '/marmots/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def marmots_index(request):
    marmots = Marmot.objects.all()
    return render(request, 'marmots/index.html', { 'marmots': marmots })

def marmots_detail(request, marmot_id):
  marmot = Marmot.objects.get(id=marmot_id)
  return render(request, 'marmots/detail.html', { 'marmot': marmot })
