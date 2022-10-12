from cats.models import Cat, Breed
from django.forms import ModelForm


class CatForm(ModelForm):
    class Meta():
        form = Cat
        fields = "__all__"
        

class BreedForm(ModelForm):
    class Meta():
        form = Breed
        fields = "__all__"