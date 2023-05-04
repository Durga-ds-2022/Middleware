from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from datetime import datetime
from django.contrib.auth.models import User
import json
# Create your models here.

class Task(models.Model):
    name= models.CharField( max_length=50)
    description= models.TextField()
    is_deleted= models.BooleanField(default=False)
    slug= models.SlugField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name

class TaskDate(models.Model):
    task= models.ForeignKey(Task, on_delete=models.CASCADE) 
    create_at= models.DateField() 
  

class History(models.Model):
    histories= models.TextField(default={})
    
    
def update_task(sender, instance, **kwargs):
        if instance.is_deleted == False:
            print("++++++++++++++++++")
            instance.save()
        print(instance)
        print("you have saved task.")

pre_save.connect(update_task, sender=Task)

@receiver(post_save, sender=Task)
def task_handler(sender, instance, **kwargs):
    print("2 way of writtig a signal")
    instance.slug= slugify(instance.name)
    print(slugify(instance.name))
    

@receiver(post_save, sender= Task)
def update_date(sender, instance, **kwargs):
    TaskDate.objects.create(task= instance, data= datetime.now())
    
    
@receiver(pre_delete, sender= Task)
def task_handler_pre_delete(sender, instance, **kwargs):
    data= {'task': instance.name, 'desc': instance.description, 'slug':instance.slug}
    History.objects.create(histories= json.dumps(data))
    
### new models for signal

class Inventory(models.Model):
    item = models.CharField(max_length=20)
    item_code = models.IntegerField()
    item_condition = models.CharField(max_length=50)
    quantity = models.IntegerField()
    def __str__(self):
        return self.item

class Order(models.Model):
    ord_number = models.CharField(max_length=20)
    inventory_item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.ord_number
    

def validate_order(sender, instance, **kwargs):
    if instance.quantity < instance.inventory_item.quantity: # order can be fulfilled
        instance.save()

pre_save.connect(validate_order, sender=Order)


def notify_user(sender, instance, **kwargs):
   print(instance.ordered_by)

post_save.connect(notify_user, sender=Order)