from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=44)
    age =models.IntegerField()
    photo=models.ImageField(upload_to='my_photo/',null=True,blank=True)

    def __str__(self):
        return f"My name is :{self.name} and I am {self.age} years old"


