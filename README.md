# Ex02 Django ORM Web Application
## Date: 25.11.2026

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Swiggy,SwiggyAdmin
admin.site.register(Swiggy,SwiggyAdmin)

models.py

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

## OUTPUT
<img width="1537" height="797" alt="Screenshot 2026-11-25 165728" src="https://github.com/user-attachments/assets/de352409-e590-45f9-9486-86343a807650" />


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
