from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from autos.forms import MakeForm
from autos.models import Make, Auto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class Mainview(LoginRequiredMixin, View):
    def get(self, request):
        soluong = Make.objects.all().count()
        all = Auto.objects.all()
        
        kontext = {'make_count': soluong, 'auto_list': all}
        return render(request, 'autos/auto_list.html', kontext)

#create more view
class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        makelist = Make.objects.all()
        kontext = {'make_list': makelist}
        return render(request, 'autos/make_list.html', kontext)
    
class MakeCreate(LoginRequiredMixin, View):
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')
    
    def get(self, request):
        form = MakeForm()
        kontext = {'form': form}
        return render(request, self.template, kontext)
    
    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        luu = form.save()
        return redirect(self.success_url)
    
    
    
    
    