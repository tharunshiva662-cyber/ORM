from django.db import models
from django.contrib import admin
class Swiggy(models.Model):
    mid=models.IntegerField()
    mname=models.CharField(max_length=100)
    price=models.IntegerField()
    quality=models.IntegerField()
    rating=models.FloatField()

class SwiggyAdmin(admin.ModelAdmin):
    list_display=('mid','mname','price','quality','rating')

