from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('marmots/', views.marmots_index, name='index'),
    path('marmots/<int:marmot_id>/', views.marmots_index, name='detail'),
]