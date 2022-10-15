from django.urls import path
from . import views
#from django.views.generic import TemplateView



app_name = 'cats'
urlpatterns = [
    path('', views.MainView.as_view(), name='allcats'),
    path('breed/', views.BreedView.as_view(), name='view_breed'),
    path('create/cat/', views.CatCreate.as_view(), name="add_cat"),
    path('create/breed/', views.BreedCreate.as_view(), name='add_breed'),
    path('delete/cat/<int:pk>/', views.CatDelete.as_view(), name='cat_delete'),
    path('delete/breed/<int:pk>/', views.BreedDelete.as_view(), name='breed_delete'),
]