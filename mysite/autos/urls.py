from django.urls import path
from . import views

app_name = 'autos'
urlpatterns = [
    path('', views.Mainview.as_view(), name='all'),
    path('lookup/', views.MakeView.as_view(), name='make_list'),
    path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),
    path('main/create/', views.AutoCreate.as_view(), name='auto_create'),
    path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
]
