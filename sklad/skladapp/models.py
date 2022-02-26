from django.contrib.auth.models import User
from django.db import models
class Ombor(models.Model):
    ism = models.CharField(max_length=100)
    dokon_nomi = models.CharField(max_length=100)
    turi = models.CharField(max_length=30,blank=True)
    manzil = models.CharField(max_length=100)
    tel = models.SmallIntegerField()
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"{self.ism}({self.dokon_nomi})"

class Product(models.Model):
    nom = models.CharField(max_length=100)
    brend_nomi = models.CharField(max_length=100)
    kelgan_narx = models.IntegerField()
    sotuvdagi_narx = models.IntegerField()
    miqdor = models.IntegerField()
    ombor = models.ForeignKey(Ombor,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"{self.nom}({self.miqdor})"

class Client(models.Model):
    dokon_nomi = models.CharField(max_length=100)
    manzil = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    ism = models.CharField(max_length=30)
    qarz = models.IntegerField(default=0)
    ombor = models.ForeignKey(Ombor,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"{self.ism}({self.dokon_nomi})"
# Create your models here.
