from django.db import models

# Create your models here.

class UserFunction(models.Model):
    first_name= models.CharField( max_length=100)
    last_name= models.CharField( max_length=100)
    email= models.EmailField( max_length=254, unique=True)
    password= models.CharField( max_length=20)
    create_date= models.DateTimeField(auto_now=True, auto_now_add=False)
    update_date= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name+ " "+ self.last_name
    