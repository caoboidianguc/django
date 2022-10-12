import re
from django import views
from django.shortcuts import redirect, render, get_object_or_404
from cats.forms import CatForm, BreedForm
from cats.models import Cat, Breed
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# Create your views here. and create all *.html to render

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        demLoai = Breed.objects.all().count()
        meo = Cat.objects.all()
        contxt = {"tong_breed": demLoai, "dsMeo": meo}
        return render(request,"cats/cats_list.html", contxt)

class BreedView(LoginRequiredMixin, View):
    htmlToRender = 'cats/breed_list.html'
    def get(self, request):
        breedlist = Breed.objects.all()
        contxt = {"breed_list": breedlist}
        return render(request, self.htmlToRender, contxt)
    
class BreedCreate(LoginRequiredMixin, View):
    success_url = reverse_lazy('cats:allcats')
    template = "cats/breed_form.html"
    def get(self, request):
        form = BreedForm()
        contxt = {"giong": form}
        return render(request, self.template, contxt)
    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            ctext = {"giong": form}
            return render(request, self.template, ctext)
        form.save()
        return redirect(self.success_url) 

class CatCreate(LoginRequiredMixin, View):
    success_url = reverse_lazy('cats:allcats')
    template = "cats/cat_form.html"
    
    def get(self, request):
        form = CatForm()
        contxt = {"form": form}
        return render(request, self.template, contxt)
    
    def post(self, request):
        form = CatForm(request.POST)
        if not form.is_valid():
            contxt = {"form": form}
            return render(request, self.template, contxt)
        cat = form.save()
        return redirect(self.success_url)