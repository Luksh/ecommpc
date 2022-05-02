from msilib.schema import Class
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.conf import settings

# Create your models here.

LABELS = (('hot','hot'),('new','new'),('sale','sale'),('','default'))

class Category(models.Model):
    name = models.CharField(max_length= 400)
    image = models.CharField(max_length= 200)
    slug = models.CharField(max_length= 500, unique= True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length= 400)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'media')
    slug = models.CharField(max_length= 500, unique= True)

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length= 400)
    image = models.ImageField(upload_to = 'media')
    title = models.TextField()
    rank = models.IntegerField(default= 1)
    status = models.CharField(max_length=25, blank=True, choices= (('active','active'),('','default')))
    description = models.TextField(blank= True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length= 400)
    image = models.ImageField(upload_to = 'media')
    title = models.TextField()
    rank = models.IntegerField(default= 1)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length= 400)
    email = models.EmailField(max_length= 300, blank= True)
    phone = models.CharField(blank= True, max_length= 200)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length= 400)
    image = models.ImageField(upload_to = 'media')
    price = models.IntegerField(default= 0)
    discounted_price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    status = models.CharField(max_length= 50, choices= (('active','active'),('inactive','inactive')))
    labels = models.CharField(max_length= 50, choices= LABELS)
    slug = models.CharField(max_length= 400, blank= True)
    description = models.TextField(blank= True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.CharField(max_length= 400)
    slug = models.CharField(max_length= 400, blank= True)
    items = models.ForeignKey(Category, on_delete = models.CASCADE)
    quantity = models.IntegerField(default= 1)
    checkout = models.BooleanField(default= False)

    def __str__(self):
        return self.name