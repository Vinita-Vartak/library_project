from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length= 100)
    category = models.CharField(max_length= 100)

    class Meta:
        abstract = True



class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_published = models.BooleanField(default= True)
    is_active = models.BooleanField(default= True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = "book"
    
    def __str__(self):
        return f"{self.name}"

    