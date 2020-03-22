from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Marmot, Toy
from .forms import FeedingForm

class MarmotCreate(CreateView):
  model = Marmot
  fields = ['name', 'species', 'description', 'age']

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
  toys_marmot_doesnt_have = Toy.objects.exclude(id__in = marmot.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'marmots/detail.html', {
    'marmot': marmot, 'feeding_form': feeding_form,
    'toys': toys_marmot_doesnt_have
  })

def add_feeding(request, marmot_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.marmot_id = marmot_id
    new_feeding.save()
  return redirect('detail', marmot_id=marmot_id)

def assoc_toy(request, marmot_id, toy_id):
  Marmot.objects.get(id=marmot_id).toys.add(toy_id)
  return redirect('detail', marmot_id=marmot_id)

def unassoc_toy(request, marmot_id, toy_id):
  Marmot.objects.get(id=marmot_id).toys.remove(toy_id)
  return redirect('detail', marmot_id=marmot_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'