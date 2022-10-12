from django.shortcuts import render, get_object_or_404
from cats.forms import CatForm, BreedForm
from cats.models import Cat, Breed
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View



# Create your views here.
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        demLoai = Breed.objects.all().count()
        meo = Cat.objects.all()
        contxt = {"tong_breed": demLoai, "dsMeo": meo}
        return render(request,"cats/cats_list.html", contxt)
