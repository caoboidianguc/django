from django.urls import path
from . import views

app_name = 'autos'
urlpatterns = [
    path('', views.Mainview.as_view(), name='all'),
    path('lookup/', views.MakeView.as_view(), name='make_list'),
    path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),
]
