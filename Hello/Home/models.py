from django.db import models


# Migrations ka matlab hai vo file generate karna jo ki is change ko generate karti hai
# Database me ye table ban jayegi jab ham ise migrate kardenge 
# after creating the models ---  make migartions 
# migrate --- apply the pending changes created by make migrations!

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=100)
    desc = models.CharField(max_length=1200)
    date = models.DateField()
    
    def __str__(self):
        return self.name


class LogIns(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
   
    def __str__(self):
        return self.username


   