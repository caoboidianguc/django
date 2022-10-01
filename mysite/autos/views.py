from django.shortcuts import render
from django.views import View
from autos.forms import MakeForm
from autos.models import Make, Auto
from django.contrib.auth.mixins import LoginRequiredMixin



class Mainview(LoginRequiredMixin, View):
    def get(self, request):
        soluong = Make.objects.all().count()
        all = Auto.objects.all()
        
        kontext = {'make_count': soluong, 'auto_list': all}
        return render(request, 'autos/auto_list.html', kontext)
    