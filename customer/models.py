from django.db import models

from account.models import CWGHMOUser
from hmo.models import Address


class Customer(models.Model):
    # Private customer model
    user = models.OneToOneField(CWGHMOUser)
    phone = models.CharField(max_length=20)
    sex = models.CharField(max_length=1, choices=(
        ('M', 'Male'),
        ('F', 'Female'),
    ))
    photo = models.ImageField(upload_to='customer/photos/')
    address = models.OneToOneField(Address)

    def __str__(self):
        return self.user.user.username


class Organization(models.Model):
    admin = models.OneToOneField(CWGHMOUser)
    name = models.CharField(max_length=50)
    address = models.OneToOneField(Address)
    contact_phone = models.CharField(max_length=20)
    contact_mail = models.EmailField()

    def __str__(self):
        return self.name


class Employee(Customer):
    organization = models.ForeignKey(Organization)
