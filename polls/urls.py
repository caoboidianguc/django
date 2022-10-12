from django.urls import path
from . import views


#nameSpace
app_name = 'polls' 
urlpatterns = [
    path('', views.index, name='index'),
    #vdu: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    #vidu: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    #vidu: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]