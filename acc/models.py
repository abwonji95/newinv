from django.db import models
from django.db.models.fields import EmailField, IntegerField



# Create your models here.
class Vendor(models.Model):
   
    date_created=models.DateTimeField(auto_now_add=True)
    vendor=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self) :
        return self.vendor

class Customer(models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self) :
        return self.name

class Engineers(models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=200,null=True)
    employee_number=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self) :
        return self.name

class Deployment(models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    engineer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    site_location=models.CharField(max_length=200,null=True)
    task=models.CharField(max_length=200,null=True)


    
class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    product_description=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    quantity=models.IntegerField(null=True)

    def __str__(self) :
        return self.name


class Services(models.Model):
    service=models.CharField(max_length=200,null=True)
    service_description=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)

    def __str__(self) :
        return self.service



    
class Order(models.Model):
    STATUS=(
            ('delivered','delivered'),('PENDING','PENDING'),
            )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    product_description=models.CharField(max_length=200,null=True)
    quantity=models.IntegerField(null=True)


class Purchases(models.Model):
    STATUS=(
            ('COMPLETED','COMPLETED'),('PENDING','PENDING'),('CANCELED','CANCELED'),
            )
    vendor=models.ForeignKey(Vendor,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    product_name=models.CharField(max_length=200,null=True)
    product_description=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    quantity=models.IntegerField(null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
   


