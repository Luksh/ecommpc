from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 400)
    image = models.ImageField(upload_to = 'media')
    slug = models.CharField(max_length= 500, unique= True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length= 400)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'media')
    slug = models.CharField(max_length= 500, unique= True)

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length= 400)
    image = models.ImageField(upload_to = 'media')
    title = models.TextField()
    description = models.TextField(blank= True)

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