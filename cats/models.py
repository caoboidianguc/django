from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator


class Cat(models.Model):
    nickname = models.CharField( max_length=50, 
                            validators=[MinLengthValidator(2, "Nick name must be greater than 1 character")] )
    weight = models.PositiveIntegerField()
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)
    foods = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return self.nickname
    
class Breed(models.Model):
    name = models.CharField(max_length=200, 
                            validators=[MinLengthValidator(2,"Breed must be greater than 1 character")])
    
    def __str__(self) -> str:
            return self.name

