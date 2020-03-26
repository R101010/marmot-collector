from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Marmot, Toy
from .forms import FeedingForm

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class MarmotCreate(LoginRequiredMixin, CreateView):
  model = Marmot
  fields = ['name', 'species', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class MarmotUpdate(LoginRequiredMixin, UpdateView):
  model = Marmot
  fields = ['species', 'description', 'age']

class MarmotDelete(LoginRequiredMixin, DeleteView):
  model = Marmot
  success_url = '/marmots/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def marmots_index(request):
  marmots = Marmot.objects.filter(user=request.user)
  return render(request, 'marmots/index.html', { 'marmots': marmots })

@login_required
def marmots_detail(request, marmot_id):
  marmot = Marmot.objects.get(id=marmot_id)
  toys_marmot_doesnt_have = Toy.objects.exclude(id__in = marmot.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'marmots/detail.html', {
    'marmot': marmot, 'feeding_form': feeding_form,
    'toys': toys_marmot_doesnt_have
  })

@login_required
def add_feeding(request, marmot_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.marmot_id = marmot_id
    new_feeding.save()
  return redirect('detail', marmot_id=marmot_id)

@login_required
def assoc_toy(request, marmot_id, toy_id):
  Marmot.objects.get(id=marmot_id).toys.add(toy_id)
  return redirect('detail', marmot_id=marmot_id)

@login_required
def unassoc_toy(request, marmot_id, toy_id):
  Marmot.objects.get(id=marmot_id).toys.remove(toy_id)
  return redirect('detail', marmot_id=marmot_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'