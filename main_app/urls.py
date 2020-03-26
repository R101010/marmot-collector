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
    path('marmots/<int:marmot_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('marmots/<int:marmot_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('marmots/<int:marmot_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]