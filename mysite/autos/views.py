from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from autos.forms import MakeForm, AutoForm
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
        make = form.save()
        return redirect(self.success_url)
    
    
#short way to create view
class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

"""
class AutoCreate(LoginRequiredMixin, View):
    template = 'autos/auto_form.html'
    
    success_url = reverse_lazy('autos:all')
    
    def get(self, request):
        form = AutoForm()
        kontext = {'form': form}
        return render(request, self.template, kontext)
    
    def post(self, request):
        form = AutoForm(request.POST)
        if not form.is_valid():
            kontext = {'form': form}
            return render(request, self.template, kontext)
        auto = form.save()
        return redirect(self.success_url)
"""

class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')
    
    def get(self, request, pk):
        layMauCu = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=layMauCu)
        kontext = {'form': form}
        return render(request, self.template, kontext)
    
    def post(self, request, pk):
        mauCu = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=mauCu)
        if not form.is_valid():
            kontext = {'form': form}
            return render(request, self.template, kontext)
        
        form.save()
        return redirect(self.success_url)

class MakeDelete():
    pass

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = 'all'
    success_url = reverse_lazy('autos:all')
    
#use reverse_lazy rather than reverse in the class attributes