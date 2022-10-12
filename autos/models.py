from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Make(models.Model):
    name = models.CharField(max_length=20,
                            help_text='Nhập hãng xe (Tesla, Dodge...)',
                            validators=[MinLengthValidator(4, "Phai co tu 4 ki tu!")])
    
    def __str__(self):
        return self.name
    
class Auto(models.Model):
    nickname = models.CharField(max_length=30, help_text='Ten xe', validators=[MinLengthValidator(3,"hon ba ki tu")])
    make = models.ForeignKey("Make", on_delete=models.CASCADE, null=False)
    mileage = models.PositiveIntegerField()
    comment = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nickname