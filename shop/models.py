from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=600)
    date = models.DateField()
    img = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    mess = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


class Checkout(models.Model):
    check_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    itemsjson = models.CharField(max_length=5000, default="")
    email = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=50, default="")
    address2 = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name
