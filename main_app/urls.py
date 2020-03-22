from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('marmots/', views.marmots_index, name='index'),
    path('marmots/<int:marmot_id>/', views.marmots_detail, name='detail'),
    path('marmots/create/', views.MarmotCreate.as_view(), name='marmots_create'),
    path('marmots/<int:pk>/update/', views.MarmotUpdate.as_view(), name='marmots_update'),
    path('marmots/<int:pk>/delete/', views.MarmotDelete.as_view(), name='marmots_delete'),
]